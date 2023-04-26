from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'employee'

designation_employee_list = views.EmployeeDesignationViewSet.as_view({'get': 'list'})

router = routers.DefaultRouter()
router.register(r'designations', views.DesignationViewSet,'designation')
router.register(r'employees', views.EmployeeViewSet,'employee')
router.register(r'designation-employees', views.EmployeeDesignationViewSet,'designation_employee')
router.register(r'appointment', views.AppointmentViewSet,'appointment')
router.register(r'banking', views.BankingViewSet, 'banking')
router.register(r'experience', views.ExperienceViewSet, 'experience')
router.register(r'education', views.EducationViewSet, 'education')
router.register(r'related-person', views.RelatedPersonViewSet, 'related_person')
router.register(r'address', views.AddressViewSet, 'address')
router.register(r'contact', views.ContactViewSet, 'contact')

urlpatterns = [
    path('', include(router.urls)),

]