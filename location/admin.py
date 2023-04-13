from django.contrib import admin
from .models import *


class regionAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(regionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['created_by'].initial = request.user
        form.base_fields['created_by'].disabled = True
        form.base_fields['created_by'].help_text = "This field is set to current_user and it's not editable"
        form.base_fields['updated_by'].initial = request.user
        form.base_fields['updated_by'].disabled = True
        form.base_fields['updated_by'].help_text = "This field is set to current_user and it's not editable"
        return form


class sub_regionAdmin(regionAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(sub_regionAdmin, self).get_form(request, obj, **kwargs)
        return form


class districtAdmin(regionAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(districtAdmin, self).get_form(request, obj, **kwargs)
        return form


class countyAdmin(regionAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(countyAdmin, self).get_form(request, obj, **kwargs)
        return form


class subcountyAdmin(regionAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(subcountyAdmin, self).get_form(request, obj, **kwargs)
        return form


class parishAdmin(regionAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(parishAdmin, self).get_form(request, obj, **kwargs)
        return form


class villageAdmin(regionAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(villageAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(district, districtAdmin)
admin.site.register(region, regionAdmin)
admin.site.register(sub_region, sub_regionAdmin)
admin.site.register(county, countyAdmin)
admin.site.register(subcounty, subcountyAdmin)
admin.site.register(parish, parishAdmin)
admin.site.register(village, villageAdmin)

# Register your models here.
