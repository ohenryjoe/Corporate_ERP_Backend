from django.db import models
from common.models import BaseModel
from common.choices import GENDER_CHOICES, LEAVE_REQUEST_STATUS, REQUESTED, LEAVE_PROCESS_MANAGER
from django.utils.functional import cached_property
from organization.models import SalaryScale
from employee.models import Employee
# Create your models here.


class LeaveType(BaseModel):
    CATEGORY =(
        ('earned','Earned'),
        ('not earned', 'Not Earned')
    )
    # Maternity Leave, Annual Leave etc
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=12, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    #add leave type category ['recurrent', 'non-recurrent']
    # if its recurrent, then it will be renewed every year
    # if its non-recurrent, then it will be renewed after a certain period

    def __str__(self):
        return self.name
    
class LeavePolicy(BaseModel):
    """
    Leave Type may have multiple leave policies
    but only one policy is active at one time
    """

    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_paid = models.BooleanField()
    # must be earned if you have worked for a certain period
    must_be_earned = models.BooleanField(default=False)
    earned_after = models.SmallIntegerField(default=0)  # in days
    is_carry_forward = models.BooleanField()
    # max days a employee can request
    total_days = models.PositiveSmallIntegerField(null=True)
    minimum_days = models.PositiveSmallIntegerField(default=1)
    # max days a employee can request at a time
    max_days_per_request = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=True, null=True
    )
    salary_scales = models.ManyToManyField(SalaryScale, related_name="leave_policies")
    # leave policy is un editable
    @cached_property
    def is_gender_specific(self) -> bool:
        return bool(self.gender)

    def __str__(self) -> str:
        return self.name

class LeavePeriod(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_policy = models.ForeignKey(LeavePolicy, on_delete=models.PROTECT)
    days_entitled = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [
            "employee",
            "leave_policy",
        ]

    def __str__(self) -> str:
        return f"Leave balance of {self.employee} for {self.leave_policy}"
    

class LeaveBalance(BaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_balances"
    )
    leave_policy = models.ForeignKey(
        LeavePolicy, on_delete=models.PROTECT, related_name="employee_leave_balances"
    )
    days_taken = models.PositiveIntegerField(default=0)  # in days
    current_balance = models.PositiveIntegerField(default=0)  # in days

    # date when leave balance will be updated; for earned leaves
    upcoming_balance_update_date = models.DateTimeField(null=True)

    class Meta:
        unique_together = [
            "employee",
            "leave_policy",
        ]

    @cached_property
    def leave_type(self):
        return self.leave_policy.leave_type.name

    def __str__(self) -> str:
        return f"Leave balance of {self.employee} for {self.leave_policy}"
    
class LeaveRequest(BaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )
    leave_policy = models.ForeignKey(
        LeavePolicy, on_delete=models.PROTECT, related_name="leave_requests"
    )
    leave_balance = models.ForeignKey(
        LeaveBalance,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leave_requests",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=15, db_index=True, choices=LEAVE_REQUEST_STATUS, default=REQUESTED
    )
    # recipient represent the immediate person to act on this leave request.
    recipient = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="received_leave_requests",
    )
    remarks = models.TextField(blank=True)

    @property
    def no_of_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self) -> str:
        return f"{self.employee} -- {self.status}"
    

class LeaveRequestStage(BaseModel):
    leave_request = models.ForeignKey(
        LeaveRequest, on_delete=models.CASCADE, related_name="stages"
    )
    actor = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="acted_leave_requests",
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    action = models.CharField(
        max_length=15,
        db_index=True,
        choices=LEAVE_PROCESS_MANAGER,
    )
    status = models.CharField(
        max_length=15,
        db_index=True,
        choices=LEAVE_REQUEST_STATUS,
        default=REQUESTED,
    )
    # forwarded_to represents the next person who will act on next stage.
    forwarded_to = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="forwared_leave_requests",
    )
    remarks = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"actor: {self.actor} -- action: {self.action} -- status: {self.status}"


class Leave(BaseModel):
    """
    Store leave distribution for a leave request

    :cvar request: leave request
    :cvar start: timestamp when leave will be applicable from
    :cvar end: timestamp till when leave for `leave_for` will be valid till

    """

    request = models.ForeignKey(
        LeaveRequest, on_delete=models.CASCADE, related_name="leaves"
    )
    start_date = models.DateField()
    end_date = models.DateField()


class LeaveProcessManager(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_managers"
    )
    leave_process = models.CharField(
        max_length=15,
        db_index=True,
        choices=LEAVE_PROCESS_MANAGER,
    )
    assigned_to = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_manager"
    )

    class Meta:
        unique_together = ["employee", "leave_process"]

# leave application workflow
# 1. employee apply for leave
# 2. leave request is forwarded to leave manager
# 3. leave manager can approve or reject leave request
# 4. if leave manager approve leave request, leave request is forwarded to hr manager
# 5. hr manager can approve or reject leave request
# 6. if hr manager approve leave request, leave request is forwarded to employee
# 7. employee can cancel leave request
# 8. if employee cancel leave request, leave request is forwarded to hr manager
# 9. hr manager can approve or reject leave request
# 10. if hr manager approve leave request, leave request is forwarded to leave manager
# 11. leave manager can approve or reject leave request
# 12. if leave manager approve leave request, leave request is forwarded to employee
# 13. employee can cancel leave request
# 14. if employee cancel leave request, leave request is forwarded to leave manager
# 15. leave manager can approve or reject leave request
# 16. if leave manager approve leave request, leave request is forwarded to hr manager
# 17. hr manager can approve or reject leave request
# 18. if hr manager approve leave request, leave request is forwarded to employee
# 19. employee can cancel leave request
# 20. if employee cancel leave request, leave request is forwarded to hr manager
# 21. hr manager can approve or reject leave request
# 22. if hr manager approve leave request, leave request is forwarded to leave manager
# 23. leave manager can approve or reject leave request
# 24. if leave manager approve leave request, leave request is forwarded to employee
# 25. employee can cancel leave request
# 26. if employee cancel leave request, leave request is forwarded to leave manager
# 27. leave manager can approve or reject leave request
# 28. if leave manager approve leave request, leave request is forwarded to hr manager
# 29. hr manager can approve or reject leave request
# 30. if hr manager approve leave request, leave request is forwarded to employee
# 31. employee can cancel leave request
# 32. if employee cancel leave request, leave request is forwarded to hr manager
# 33. hr manager can approve or reject leave request
# 34. if hr manager approve leave request, leave request is forwarded to leave manager