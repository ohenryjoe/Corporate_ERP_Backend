from django.db import models
from common.models import BaseModel
from django.utils import timezone
import datetime
from common.choices import (APPOINTMENT_CAPACITY_CHOICES)
# Create your models here.
class SalaryScale(BaseModel):
    '''This model handles the salary scale'''
    scale = models.CharField(max_length=255)
    rank_order = (
        models.PositiveIntegerField()
    )  # e.g 1, 2, 3 etc the smaller, the more senior # unique as well
    title = models.CharField(max_length=255)  # e.g Principal Officer
    rank_description = models.TextField(blank=True, null=True)  # e.g Heads a Section

    def __str__(self) -> str:
        return self.scale + '  ------  ' + self.title
    
class CorporateEntity(BaseModel):
    """This model handles the corporate structure"""

    # rank denotes the hierarchical position of a entity
    rank = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    headed_by = models.ForeignKey(SalaryScale, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
    
class Unit(BaseModel):
    """This model handles the different units"""
    title = models.CharField(max_length=255)
    entity = models.ForeignKey(CorporateEntity, related_name="entity", on_delete=models.SET_NULL, null=True)
    parent_entity = models.ForeignKey(CorporateEntity, related_name="parententity", on_delete=models.SET_NULL,
                                      null=True)
    parent_unit = models.ForeignKey("self", related_name="parentunit", on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title

class Event(BaseModel):
    ''' All events are published here'''
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    start_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255, default='UNEB Kyambogo Offices')
    attachment = models.FileField(upload_to="uploads/events/")

    def __str__(self):
        return self.title
    
class Notice(BaseModel):
    ''' All notices are published here'''
    title = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    caption = models.CharField(max_length=255)
    detail = models.TextField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    attachment = models.FileField(
        upload_to="uploads/notices/"
    )

    def __str__(self):
        return self.title
    
class EmploymentTenure(BaseModel):
    ''' Contract, Permanent e.t.c '''
    code = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class EmploymentType(BaseModel):
    ''' includes part-time, full-time etc'''
    code = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# class Designation(BaseModel):
#     ''' This model handles the different designations'''
#     title = models.CharField(max_length=255)
#     short_name = models.CharField(max_length=255, blank=True, null=True)
#     org_unit = models.ForeignKey(Unit, default=1, on_delete=models.SET_DEFAULT, related_name='orgunit')
#     is_supervisory = models.BooleanField()
#     employment_type = models.ForeignKey(EmploymentType, related_name="emp_type", on_delete=models.SET_NULL, null=True, )
#     # probation period in months
#     probation_period = models.PositiveSmallIntegerField(default=6)
#     employment_tenure = models.ForeignKey(EmploymentTenure, related_name="emp_tenure", on_delete=models.SET_NULL,
#                                           null=True)
#     job_summary = models.TextField(blank=True)
#     job_description = models.TextField(blank=True)
#     headed_by = models.ForeignKey(
#         'self', on_delete=models.SET_NULL, null=True, blank=True,
#     )
#     max_holders = models.PositiveSmallIntegerField(default=1)  # how many officers can hold this position concurrently?
#     salary_scale = models.ForeignKey(
#         SalaryScale, on_delete=models.SET_NULL, null=True, blank=True,
#     )
#     supervisor = models.ForeignKey(
#         "users.User", on_delete=models.SET_NULL, null=True, blank=True
#     )

#     def __str__(self):
#         return self.title

# move to employee
# class Appointment(BaseModel):
#     ''' This model handles the appointment of employees to different positions'''
#     employee = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="appointment")
#     designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="appointment_designation")
#     capacity = models.CharField(max_length=20, choices=APPOINTMENT_CAPACITY_CHOICES, )
#     start_date = models.DateField(default=datetime.date.today)
#     end_date = models.DateField(blank=True, null=True)
#     title = models.CharField(max_length=255)
#     file = models.FileField(
#         upload_to="uploads/appointment_letters/"
#     )
# all information related to employment must move to appointment