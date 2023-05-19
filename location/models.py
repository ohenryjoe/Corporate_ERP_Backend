import uuid
from django.db import models
from accounts.models import User


# Create your models here.
class region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='region_update_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'


class sub_region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, to_field="code", on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='sub_region_update_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Regions'
        verbose_name = 'Sub Region'


class district(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_region = models.ForeignKey(sub_region, default=None,to_field="code", on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, default=None, )
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='district_update_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'


class local_government(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    district = models.ForeignKey(district, default=None,to_field="code", on_delete=models.PROTECT)
    vote_code = models.CharField(max_length=100,unique=True, default=None)
    name = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='update_loc_gov_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Local Government'
        verbose_name = 'Local Governments'


class county(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    district = models.ForeignKey(district, default=None, to_field="code", on_delete=models.PROTECT)
    local_gov = models.ForeignKey(local_government, default=None, to_field="vote_code", on_delete=models.PROTECT)
    vote_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True)
    constituency = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='update_country_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Counties'
        verbose_name = 'County'


class subcounty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    county = models.ForeignKey(county, default=None, to_field="vote_code", on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, unique=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='sub_country_update_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Counties'
        verbose_name = 'Sub County'


class parish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subcounty = models.ForeignKey(subcounty, default=None, to_field="code", on_delete=models.PROTECT)
    postcode = models.CharField(max_length=5, default=None)
    code = models.CharField(max_length=20, default=None, unique=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='parish_update_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Parishes'
        verbose_name = 'Parish'

    def __str__(self):
        return self.name


class village(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parish = models.ForeignKey(parish, default=None, to_field="code", on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, unique=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, default=None, on_delete=models.PROTECT, null=True, blank=True, related_name='village_update_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Villages'
        verbose_name = 'Village'
