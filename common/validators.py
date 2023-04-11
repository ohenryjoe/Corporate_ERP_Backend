from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings

def is_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Cannot be a past date")
    return value
# TODO add dynamic setting in the admin panel
def validate_user_birth_date(value):
    age = (timezone.now().date() - value).days / 365
    if age < settings.MIN_USER_AGE or age > settings.MAX_USER_AGE:
        raise ValidationError(
            f"Invalid birth date. Age must be between {settings.MIN_USER_AGE} and {settings.MAX_USER_AGE}"
        )
    return value