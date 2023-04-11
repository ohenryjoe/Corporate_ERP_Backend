from django.urls import path, include
from rest_framework import routers
from .views import (MyTokenObtainPairView,
                     LogoutAndBlacklistRefreshTokenForUserView,UserViewSet
                     )
from rest_framework_simplejwt import views as jwt_views



app_name = 'accounts'

router = routers.DefaultRouter()

#router.register(r'register', UserViewSet, basename='register')
#router.register(r'my_profile', MyProfileAPI, 'my_profile')
router.register(r'users', UserViewSet, 'usersprofiles')

urlpatterns = [

    # api/accounts/
    path('', include(router.urls)),

    path('login', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   # path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('logout', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
   # path('password_reset/',ResetPasswordRequestToken.as_view(), name='password_reset'),
   # path('password_reset/confirm/', ResetPasswordConfirm.as_view(),name='reset-password-confirm'),
   
]
