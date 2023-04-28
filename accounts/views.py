from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import (filters, parsers, permissions, renderers, status,
                            viewsets)
from .models import User
from .serializers import UserSerializer
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
    
# Create your views here.

# using Simple JWT to generate user token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# blacklist tokens


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e, ", sorry  I can't log you out")
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage system users  data'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['email','first_name','last_name','gender']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = User.objects.all().order_by('-id')
       
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Admin').exists():
            queryset = queryset
        else:
            user = self.request.user
            queryset = queryset.filter(id=user.id)

        return queryset
    
    