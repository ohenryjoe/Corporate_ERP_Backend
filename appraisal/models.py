from django.db import models
from common.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from accounts.models import User
from common.choices import AppraisalScheduleStatusChoices

# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class AppraisalFrequency(BaseModel):
    title = models.CharField(max_length=50, null=False, blank=False)
    # duration in months
    duration = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    is_for_probational = models.BooleanField(default=False, db_index=True)
    is_adhoc = models.BooleanField(default=False, db_index=True)

    def __str__(self) -> str:
        return self.title


class AppraisalPerformanceFactor(BaseModel):
    """
    Sample data of this table:

        title: Time Management
        scores: [
                    {"score": 5, "description": "Best time management", "remarks": "Excellent"},
                    {"score": 4, "description": "V.Good time management", "remarks": "V.good"},
                    {"score": 3, "description": "Good time management", "remarks": "Good"},
                ]
        created_by: 1 // id of user

        Validation for json field is handeled by serializers upon creation
    """

    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(blank=True)
    scores = models.JSONField(default=list)
    created_by = models.ForeignKey(
        User,
        related_name="created_performance_factors",
        null=True,
        on_delete=models.DO_NOTHING,
    )


class AppraisalSchedule(BaseModel):
    """
    This model resembles the period of employment for which a employee is getting appraised
    """

    frequency = models.ForeignKey(
        AppraisalFrequency,
        on_delete=models.SET_NULL,
        related_name="appraisal_schedules",
        null=True,
        blank=True,
    )
    appraisee = models.ForeignKey(
        User, related_name="appraisal_schedules", on_delete=models.CASCADE
    )
    appraiser = models.ForeignKey(
        User, related_name="as_appraiser", on_delete=models.SET_NULL, null=True
    )

    # working period that a appraisal resembles
    start_date = models.DateField()
    end_date = models.DateField()

    # period to perform appraisal
    appraisal_opened_at = models.DateField()
    appraisal_deadline_date = models.DateField()

    status = models.CharField(
        max_length=50,
        choices=AppraisalScheduleStatusChoices.choices,
        default=AppraisalScheduleStatusChoices.KRA_DATA_PENDING,
    )

    class Meta:
        unique_together = ["frequency", "appraisee", "start_date"]

    def __str__(self) -> str:
        return f"Appraisee: {self.appraisee} - Start-Date: {self.start_date} - Status:{self.status}"


class AppraiseePerformanceIndicator(BaseModel):
    """
    Holds data of a performance indicator of a particular appraisee
    If a appraisal is completed then is_active is set to False

    Sample data of this Model:

        appraisal_schedule: 1 //id of AppraisalSchedule
        performance_indicators: [
            {
                'output: 'Code Optimization',
                'performance_target': 'Overall Optimization',
                'performance_indicator': 'Optimized code by 50%',
                'max_score': 5
            },
            {
                'output: 'DB Optimization',
                'performance_target': 'DB Optimization',
                'performance_indicator': 'Optimized db by 50%',
                max_score: 5
            }
        ]
        Validation for json field is handeled by serializers upon creation

    """

    appraisal_schedule = models.OneToOneField(
        AppraisalSchedule,
        on_delete=models.CASCADE,
        related_name="performance_indicator",
        null=True,
    )
    performance_indicators = models.JSONField(default=list)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        """
        Only a instance can be active w.r.t a particular appraisee
        """
        if self.is_active:
            qs = type(self).objects.filter(is_active=True, appraisee=self.appraisee)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                ValidationError(
                    "Only one performance indicator can be active for a particular user"
                )


class Appraisal(BaseModel):
    schedule = models.OneToOneField(
        AppraisalSchedule, on_delete=models.CASCADE, related_name="appraisal"
    )

    self_reviewed_at = models.DateTimeField(null=True)
    supervisor_reviewed_at = models.DateTimeField(null=True)
    supervisor_pffs_reviewed_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    # Key Related Areas (Output of employees)
    KRA_data = models.JSONField(default=list)
    KRA_total_score = models.FloatField(default=0, validators=[MinValueValidator(0)])
    KRA_total_obtained_score = models.FloatField(
        default=0, validators=[MinValueValidator(0)]
    )
    KRA_total_percentage = models.DecimalField(
        max_digits=3, decimal_places=0, default=0.0, validators=PERCENTAGE_VALIDATOR
    )

    # Performance factor and Standard Score (Already defined set of standards)
    PFSS_data = models.JSONField(default=list)
    PFSS_total_percentage = models.DecimalField(
        max_digits=3, decimal_places=0, default=0.0, validators=PERCENTAGE_VALIDATOR
    )

    total_percentage = models.DecimalField(
        max_digits=3, decimal_places=0, default=0.0, validators=PERCENTAGE_VALIDATOR
    )

    class Meta:
        ordering = [
            "-created_at",
        ]



class PerformanceImprovementPlan(BaseModel):
    appraisal_schedule = models.OneToOneField(
        AppraisalSchedule,
        on_delete=models.CASCADE,
        null=True,
        related_name="performance_improvement",
    )
    data = models.JSONField(default=list)