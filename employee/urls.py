from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'employee'


router = routers.DefaultRouter()
router.register(r'designations', views.DesignationViewSet,'designation')
router.register(r'employees', views.EmployeeViewSet,'employees')



urlpatterns = [
    path('', include(router.urls)),

]