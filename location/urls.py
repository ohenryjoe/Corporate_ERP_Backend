from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'location'

router = routers.DefaultRouter()
router.register(r'region', RegionViewSet,'region')
router.register(r'subregion', SubRegionViewSet,'subregion')
router.register(r'district', DistrictViewSet,'district')
router.register(r'local-govt', DistrictViewSet,'local_govt')
router.register(r'county', CountyViewSet,'county')
router.register(r'subcounty', SubCountyViewSet,'subcounty')
router.register(r'parish', ParishViewSet,'parish')
router.register(r'village', VillageViewSet,'village')

urlpatterns = [
    path('', include(router.urls)),
]