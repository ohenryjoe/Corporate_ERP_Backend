from django.db import models

# Create your models here.
from django.db import models

from cuser.fields import CurrentUserField
from .utils import unique_slugify


class BaseModel(models.Model):
    """
    Base model for this project.
    """

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    archived_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class CuserModel(models.Model):
    created_by = CurrentUserField(
        add_only=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
        null=True,
    )

    modified_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        abstract = True


class SlugModel(models.Model):
    """
    Abstract model to insert slug field in model

    Takes reference from fields `name` or `title` and create
    slug for that instance before saving.
    """

    slug = models.SlugField(unique=True, max_length=255, blank=True)

    class Meta:
        abstract = True

    def get_slug_text(self):
        slug_text = None
        if hasattr(self, "alt_name"):
            slug_text = self.alt_name.lower()
        elif hasattr(self, "name"):
            slug_text = self.name.lower()
        elif hasattr(self, "title"):
            slug_text = self.title.lower()
        assert (
            slug_text is not None
        ), "There must be a field named `name` or `title` or `alt name`"
        return slug_text

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = self.get_slug_text()
            unique_slugify(self, slug_text)
        if self.slug and self.slug.startswith("copy-of"):
            slug_text = self.get_slug_text()
            unique_slugify(self, slug_text)
        return super().save(*args, **kwargs)


class AbstractBaseModel(BaseModel, SlugModel, CuserModel):
    class Meta:
        abstract = True

