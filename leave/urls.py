from django.urls import path, include
from rest_framework import routers
from leave import views


app_name = 'leave'


router = routers.DefaultRouter()
router.register(r'leave-types', views.LeaveTypeViewSet,'leave_types')
router.register(r'leave-policies', views.LeavePolicyViewSet, 'leave_policies')
# router.register(r'sub-regions', views.SubRegionViewSet, 'sub_regions')
# router.register(r'districts', views.DistrictViewSet, 'districts')
# router.register(r'local-government', views.LocalGovernmentViewSet, 'local_government')
# router.register(r'counties', views.CountyViewSet, 'counties')
# router.register(r'sub-counties', views.SubCountyViewSet, 'sub_counties')
# router.register(r'parishes', views.ParishViewSet, 'parishes')
# router.register(r'villages', views.VillageViewSet, 'villages')



urlpatterns = [
    path('', include(router.urls)),

]