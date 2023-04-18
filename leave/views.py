from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import LeaveType, LeavePolicy
from .serializers import LeaveTypeSerializer, LeavePolicySerializer

# Create your views here.
class LeaveTypeViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for nationality data'''
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class LeavePolicyViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Leave Policy data'''
    queryset = LeavePolicy.objects.all()
    serializer_class = LeavePolicySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','leave_type__name','description','is_paid']
    ordering_fields = '__all__'