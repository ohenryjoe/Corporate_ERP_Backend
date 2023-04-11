from django.shortcuts import render
from rest_framework import viewsets,permissions,filters
from .serializers import DesignationSerializer, EmployeeSerializer
from .models import Designation,Employee

# Create your views here.
class DesignationViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for Designation data'''
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title','short_name','job_summary','job_description',]
    ordering_fields = '__all__'

class EmployeeViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud  for employee data'''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__first_name','user__last_name','designation__title','joined_date',]
    ordering_fields = '__all__'
