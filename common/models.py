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

class Region(BaseModel):
    
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'


class SubRegion(BaseModel):
    
    region = models.ForeignKey(Region, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Regions'
        verbose_name = 'Sub Region'


class District(models.Model):
    
    sub_region = models.ForeignKey(SubRegion, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100, default=None, )
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'


class LocalGovernment(models.Model):
    district = models.ForeignKey(District, default=None, on_delete=models.PROTECT)
    vote_code = models.CharField(max_length=100,null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Local Government'
        verbose_name = 'Local Governments'


class County(models.Model):
    district = models.ForeignKey(District, default=None, on_delete=models.PROTECT)
    local_gov = models.ForeignKey(LocalGovernment, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)
    constituency = models.CharField(max_length=100, null=True, blank=True)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Counties'
        verbose_name = 'County'


class SubCounty(models.Model):
    county = models.ForeignKey(County, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, unique=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Counties'
        verbose_name = 'Sub County'


class Parish(models.Model):
    subcounty = models.ForeignKey(SubCounty, default=None, on_delete=models.PROTECT)
    postcode = models.CharField(max_length=5, default=None)
    code = models.CharField(max_length=20, default=None, )
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
   

    class Meta:
        verbose_name_plural = 'Parishes'
        verbose_name = 'Parish'

    def __str__(self):
        return self.name


class Village(models.Model):
    parish = models.ForeignKey(Parish, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, )
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Villages'
        verbose_name = 'Village'