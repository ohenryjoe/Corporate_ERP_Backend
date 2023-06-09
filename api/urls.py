"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ERP ISMIS API",
      default_version='v1',
      description="ERP ISMIS API",
      terms_of_service="https://uneb.ac.ug/",
      contact=openapi.Contact(email="mail@uneb.ac.ug"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls', namespace="accounts")),
    path('api/common/', include('common.urls', namespace="common")),
    path('api/organization/', include('organization.urls', namespace="organization")),
    path('api/location/', include('location.urls', namespace="location")),
    path('api/leave/', include('leave.urls', namespace="leave")),
    path('api/appraisal/', include('appraisal.urls', namespace="appraisal")),
    path('api/employee/', include('employee.urls', namespace="employee")),
    re_path(r'^$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
