import datetime

from django.db import models
from common.models import BaseModel, Nationality
from accounts.models import User
from common.validators import validate_user_birth_date
from common.choices import GENDER_CHOICES, SALUTATION_CHOICES, MARITAL_CHOICES
from core.models import CuserModel
from employee.constants import ADDRESS_TYPE, QUALIFICATION_LEVEL_CHOICES, RELATIONSHIP_TYPE, \
    APPOINTMENT_CAPACITY_CHOICES
from organization.models import Unit, EmploymentType, EmploymentTenure, SalaryScale


# Create your models here.

class Employee(BaseModel, CuserModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="detail", null=False, blank=True)
    employeeNumber = models.CharField(max_length=10, blank=True, null=True)
    surname = models.CharField(max_length=25, blank=False, null=False)
    othernames = models.CharField(max_length=25, blank=False, null=False)
    dob = models.DateField(validators=[validate_user_birth_date])
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=15, default='Female'
    )
    salutation = models.CharField(
        choices=SALUTATION_CHOICES, max_length=15, default='Ms'
    )
    nationality = models.ForeignKey(Nationality, on_delete=models.RESTRICT, null=True, blank=False)
    marital_status = models.CharField(
        choices=MARITAL_CHOICES, max_length=15, blank=True
    )
    profilePic = models.FileField(upload_to="profilePic/", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone1 = models.IntegerField(null=False)
    phone2 = models.IntegerField(null=True)
    religion = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.employeeNumber

class Designation(BaseModel, CuserModel):
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
    # supervisor must be a user or an employee
    supervisor = models.ForeignKey('self', null=True,blank=True, on_delete=models.SET_NULL, related_name='designation_supervisor'
                                   )

    def __str__(self):
        return self.title





class Appointment(BaseModel):
    ''' This model handles the appointment of employees to different positions'''
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="appointment")
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="appointment_designation")
    capacity = models.CharField(max_length=20, choices=APPOINTMENT_CAPACITY_CHOICES, )
    employment_type = models.ForeignKey(EmploymentType, default=1, on_delete=models.PROTECT)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to="appointment_letters/")
    first_appointment = models.BooleanField(default=False)
    current_appointment = models.BooleanField(default=False)

    # class Meta:
    #     unique_together = ['employee', 'capacity', 'current_appointment']


class Banking(BaseModel, CuserModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    accountName = models.CharField(max_length=25, blank=False, null=False)
    accountNumber = models.IntegerField(blank=False, null=False)
    bankName = models.CharField(max_length=25, blank=False, null=False)


class Experience(BaseModel, CuserModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="experience")
    job_title = models.CharField(max_length=50, blank=True)
    org_name = models.CharField(max_length=50, blank=True)
    org_website = models.CharField(max_length=50, blank=True)
    org_telephone = models.CharField(max_length=50, blank=True)
    org_email = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    # to_date = models.DateField(widget=MonthYearWidget(years=xrange(2004, 2010)))


class Education(BaseModel, CuserModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="education")
    qualification_title = models.CharField(max_length=150, blank=True)
    qualification_Level = models.CharField(choices=QUALIFICATION_LEVEL_CHOICES, max_length=50, blank=True)
    institution_name = models.CharField(max_length=150, default=None)
    institution_website = models.CharField(max_length=150, null=True, blank=True)
    institution_address = models.TextField(null=True, blank=True)
    institution_email = models.EmailField(null=True, blank=True)
    qualification_description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)


class RelatedPerson(BaseModel, CuserModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=15, default=None)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    date_of_birth = models.DateField(null=True, max_length=150, blank=True, )
    nin = models.CharField(max_length=14, blank=True, null=True)
    relationship = models.CharField(choices=RELATIONSHIP_TYPE, max_length=150, blank=True)
    is_nok = models.BooleanField(default=False)
    is_dependant = models.BooleanField(default=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, default=None)
    address = models.CharField(max_length=255, default=None)


class Address(BaseModel, CuserModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='address')
    region = models.CharField(max_length=15, default=None)
    district = models.CharField(max_length=15, default=None)
    county = models.CharField(max_length=15, default=None)
    subcounty = models.CharField(max_length=15, default=None)
    parish = models.CharField(max_length=15, blank=True)
    village = models.CharField(max_length=15, blank=True)


class Contact(BaseModel, CuserModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='contact')
    contact_type = models.CharField(choices=ADDRESS_TYPE, max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, default=None)
