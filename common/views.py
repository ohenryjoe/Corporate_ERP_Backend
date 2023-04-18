from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializer import NationalitySerializer
from .models import Nationality

# Create your views here.
class NationalityViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for nationality data'''
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

