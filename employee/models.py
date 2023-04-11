from django.db import models
from common.models import BaseModel,Nationality, Village
from accounts.models import User
from common.validators import validate_user_birth_date
from common.choices import SALUTATION_CHOICES, MARITAL_CHOICES
from organization.models import Unit, EmploymentType, EmploymentTenure, SalaryScale

# Create your models here.



class Designation(BaseModel):
    ''' This model handles the different designations'''
    title = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    org_unit = models.ForeignKey(Unit, default=1, on_delete=models.SET_DEFAULT, related_name='orgunit')
    is_supervisory = models.BooleanField()
    employment_type = models.ForeignKey(EmploymentType, related_name="emp_type", on_delete=models.SET_NULL, null=True, )
    # probation period in months
    probation_period = models.PositiveSmallIntegerField(default=6)
    employment_tenure = models.ForeignKey(EmploymentTenure, related_name="emp_tenure", on_delete=models.SET_NULL,
                                          null=True)
    job_summary = models.TextField(blank=True)
    job_description = models.TextField(blank=True)
    headed_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
    )
    max_holders = models.PositiveSmallIntegerField(default=1)  # how many officers can hold this position concurrently?
    salary_scale = models.ForeignKey(
        SalaryScale, on_delete=models.SET_NULL, null=True, blank=True,
    )
    supervisor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title

class Employee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="detail")
    dob = models.DateField(validators=[validate_user_birth_date])
    designation = models.ForeignKey(
        Designation,
        related_name="users",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    contract_duration = models.IntegerField(null=True, blank=True)
    salutation = models.CharField(
        choices=SALUTATION_CHOICES, max_length=15, default='Mr'
    )
    nationality = models.ForeignKey(Nationality, on_delete=models.RESTRICT, null=True, blank=False)
    marital_status = models.CharField(
        choices=MARITAL_CHOICES, max_length=15, blank=True
    )
    employee_number = models.CharField(max_length=50, blank=True)
    employment_type = models.ForeignKey(
        EmploymentType, related_name="users", on_delete=models.SET_NULL, null=True
    )
    # probation period in months
    probation_period = models.PositiveSmallIntegerField(default=3)
    employment_tenure = models.ForeignKey(
        EmploymentTenure, related_name="users", on_delete=models.SET_NULL, null=True
    )
    salary_scale = models.ForeignKey(
        SalaryScale, on_delete=models.SET_NULL, null=True, blank=True
    )
    joined_date = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey(
        User, related_name="approved_users", on_delete=models.SET_NULL, null=True
    )
    file = models.FileField(upload_to="uploads/appointment_letters/", null=True)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, blank=True)
    # is_approved will hold approved status even if approved_by user is deleted
    is_approved = models.BooleanField(default=False)
    supervisor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="underlings",
    )
    

    def __str__(self):
        return self.name

