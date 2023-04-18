from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    Base model for this project.
    """

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    archived_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Nationality(BaseModel):
    name = models.CharField (max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

