from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'organization'


router = routers.DefaultRouter()
router.register(r'salary-scale', views.SalaryScaleViewSet,'salary_scale')
router.register(r'corporate-entities', views.CorporateEntityViewSet,'corporate_entity')
router.register(r'units', views.UnitViewSet,'unit')
router.register(r'events', views.EventViewSet,'event')
router.register(r'notice', views.NoticeViewSet,'notice')
router.register(r'employment-types', views.EmploymentTypeViewSet, 'employment_types')
router.register(r'employment-tenures', views.EmploymentTenureViewSet, 'employment_tenures')


urlpatterns = [
    path('', include(router.urls)),

]