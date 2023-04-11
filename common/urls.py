from django.urls import path, include
from rest_framework import routers
from common import views


app_name = 'persons_with_disabilites'


router = routers.DefaultRouter()
router.register(r'nationalities', views.NationalityViewSet,'nationalities')
router.register(r'regions', views.RegionViewSet, 'regions')
router.register(r'sub-regions', views.SubRegionViewSet, 'sub_regions')
router.register(r'districts', views.DistrictViewSet, 'districts')
router.register(r'local-government', views.LocalGovernmentViewSet, 'local_government')
router.register(r'counties', views.CountyViewSet, 'counties')
router.register(r'sub-counties', views.SubCountyViewSet, 'sub_counties')
router.register(r'parishes', views.ParishViewSet, 'parishes')
router.register(r'villages', views.VillageViewSet, 'villages')



urlpatterns = [
    path('', include(router.urls)),

]