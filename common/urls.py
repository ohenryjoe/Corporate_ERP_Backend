from django.urls import path, include
from rest_framework import routers
from common import views


app_name = 'persons_with_disabilites'


router = routers.DefaultRouter()
router.register(r'nationalities', views.NationalityViewSet,'nationalities')


urlpatterns = [
    path('', include(router.urls)),

]