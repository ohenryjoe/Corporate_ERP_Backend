from django.urls import path, include
from rest_framework import routers
from appraisal import views


app_name = 'appraisal'


router = routers.DefaultRouter()
router.register(r'appraisal-frequencies', views.AppraisalFrequencyViewSet,'appraisal_frequency')
router.register(r'appraisal-performance-factors', views.AppraisalPerformanceFactorViewSet, 'appraisal_performance_ factor')
router.register(r'appraisal-schedules', views.AppraisalScheduleViewSet, 'appraisal_schedules')
# router.register(r'districts', views.DistrictViewSet, 'districts')
# router.register(r'local-government', views.LocalGovernmentViewSet, 'local_government')
# router.register(r'counties', views.CountyViewSet, 'counties')
# router.register(r'sub-counties', views.SubCountyViewSet, 'sub_counties')
# router.register(r'parishes', views.ParishViewSet, 'parishes')
# router.register(r'villages', views.VillageViewSet, 'villages')



urlpatterns = [
    path('', include(router.urls)),

]