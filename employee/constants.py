import datetime

MALE, FEMALE, OTHER = "Male", "Female", "Other"

GENDER_CHOICES = [(MALE, "Male"), (FEMALE, "Female"), (OTHER, "Other")]

SUBSTANTIVE, ACTING = "Substantive", "Acting"
APPOINTMENT_CAPACITY_CHOICES = [(SUBSTANTIVE, "Substantive"), (ACTING, "Acting")]

MISTER, MISS, MRS = "Mr.", "Ms.", "Mrs."
DOCTOR, ENGINEER, PROFESSOR, HONOURABLE = (
    "Dr.",
    "Eng.",
    "Prof.",
    "Hon.",
)

SALUTATION_CHOICES = [
    (MISTER, "Mr."),
    (MISS, "Ms."),
    (MRS, "Mrs."),
    (DOCTOR, "Dr."),
    (ENGINEER, "Eng."),
    (PROFESSOR, "Prof."),
    (HONOURABLE, "Hon."),
]

UGANDA, KENYA, RWANDA, BURUNDI = "Uganda", "Kenya", "Rwanda", "Burundi"
SOUTH_SUDAN, TANZANIA, NON_EAC_COUNTRY = "South Sudan", "Tanzania", "Non EAC Country"

NATIONALITY_CHOICES = [
    (UGANDA, "Uganda"),
    (KENYA, "Kenya"),
    (RWANDA, "Rwanda"),
    (SOUTH_SUDAN, "South Sudan"),
    (BURUNDI, "Burundi"),
    (TANZANIA, "Tanzania"),
    (NON_EAC_COUNTRY, "Non EAC Country"),
]

MARRIED, SINGLE, WIDOWED, DIVORCED = "Married", "Single", "Widowed", "Divorced"
MARITAL_CHOICES = [
    (MARRIED, "Married"),
    (SINGLE, "Single"),
    (WIDOWED, "Widowed"),
    (DIVORCED, "Divorced"),
]
QUALIFICATION_LEVEL_CHOICES = [
    ('Post-Doctorate', "Post-Doctorate"),
    ('Doctorate', "Doctorate"),
    ('Masters', "Masters"),
    ('PGD', "post Graduate Diploma"),
    ('Bachelors', "Bachelors"),
    ('Diploma', "Diploma"),
    ('Certificate', "Certificate"),
    ('UACE', "Advanced Certificate of Education"),
    ('UCE', "Ordinary Certificate of Education"),
    ('PLE', "Primary Leaving Examination Certificate"),
]

RELATIONSHIP_TYPE = [
    ('Spouse', "Spouse"),
    ('Child', "Child"),
    ('Mother', "Mother"),
    ('Father', "Father"),
    ('Guardian', "Guardian"),
]

ADDRESS_TYPE = [
    ('Permanent', "Permanent"),
    ('Residential', "Residential"),
]

RETIREMENT_AGE = 60

CURRENT_YEAR = datetime.date.today().year

SWOT_CATEGORY = [
    ('Strength', "Strength"),
    ('Weakness', "Weakness"),
    ('Opportunity', "Opportunity"),
    ('Threat', "Threat"),
]
ACTIVITY_STATUS = [
    ('planned', "planned"),
    ('on-going', "on-going"),
    ('on-hold', "on-hold"),
    ('completed', "completed"),
]

TASK_PRIORITY = [
    ('very-urgent', "very-urgent"),
    ('urgent', "urgent"),
    ('normal', "normal"),
    ('can-wait', "can-wait"),
]

MEASURED_AS = [
    ('Percentage', "Percentage"),
    ('Number', "Number"),
]

DAY_OPTIONS = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('30', '30'),
    ('31', '31'),
]

MONTH_OPTIONS = [
    ('JANUARY', 'JAN'),
    ('FEBRUARY', 'FEB'),
    ('MARCH', 'MAR'),
    ('APRIL', 'APR'),
    ('MAY', 'MAY'),
    ('JUNE', 'JUN'),
    ('JULY', 'JUL'),
    ('AUGUST', 'AUG'),
    ('SEPTEMBER', 'SEP'),
    ('OCTOBER', 'OCT'),
    ('NOVEMBER', 'NOV'),
    ('DECEMBER', 'DEC')
]
