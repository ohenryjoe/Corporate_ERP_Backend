from django.db import models

SUBSTANTIVE, ACTING = "Substantive", "Acting"
APPOINTMENT_CAPACITY_CHOICES = [(SUBSTANTIVE, "Substantive"), (ACTING, "Acting")]
GENDER_CHOICES = (
    ('Male', "Male"), 
    ('Female', "Female")
)

SALUTATION_CHOICES = (
    ('Mr', "Mr."),
    ('Ms', "Ms."),
    ('Mrs', "Mrs."),
    ('Dr', "Dr."),
    ('Eng', "Eng."),
    ('Prof', "Prof."),
    ('Hon', "Hon."),
)

MARITAL_CHOICES =(
     ('Married', "Married"),
    ('Single', "Single"),
    ('Widowed', "Widowed"),
    ('Divorced', "Divorced"),
)

REQUESTED = "Requested"
VERIFIED = "Verified"
PREAPPROVED = "Preapproved"
APPROVED = "Approved"
GRANTED = "Granted"
DENIED = "Denied"
CANCELED = "Canceled"

VERIFIER = "Verifier"
PREAPPROVER = "Preapprover"
APPROVER = "Approver"
GRANTER = "Granter"

LEAVE_REQUEST_STATUS = (
    (REQUESTED, REQUESTED),
    (VERIFIED, VERIFIED),
    (APPROVED, APPROVED),
    (PREAPPROVED, PREAPPROVED),
    (GRANTED, GRANTED),
    (DENIED, DENIED),
    (CANCELED, CANCELED),
)

LEAVE_PROCESS_MANAGER = (
    (VERIFIER, VERIFIER),
    (PREAPPROVER, PREAPPROVER),
    (APPROVER, APPROVER),
    (GRANTER, GRANTER),
)


class AppraisalScheduleStatusChoices(models.TextChoices):
    KRA_DATA_PENDING = "KRA Data Pending"
    KRA_DATA_FILLED = "KRA Data Filled"
    STARTED = "Appraisal Evaluation Started"
    SELF_REVIEW_COMPLETED = "Self Review Completed"
    SUPERVISOR_REVIEW_KRA_COMPLETED = "Supervisor KRA Review Completed"
    SUPERVISOR_REVIEW_PF_COMPLETED = "Supervisor Performance Factor Review Completed"
    APPRAISAL_COMPLETED = "Completed"