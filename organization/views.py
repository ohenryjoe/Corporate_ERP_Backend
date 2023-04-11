from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from .models import SalaryScale, CorporateEntity, Unit, Event, Notice
from .serializers import SalaryScaleSerializer, CorporateEntitySerializer, UnitSerializer, EventSerializer, NoticeSerializer


# Create your views here.


class SalaryScaleViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for salary scale data'''
    queryset = SalaryScale.objects.all()
    serializer_class = SalaryScaleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['scale','title','rank_description']
    ordering_fields = '__all__'


class CorporateEntityViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for corporate entity data'''
    queryset = CorporateEntity.objects.all()
    serializer_class = CorporateEntitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['rank','title','description']
    ordering_fields = '__all__'


class UnitViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for unit data'''
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title','description']
    ordering_fields = '__all__'


class EventViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for event data'''
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title','caption','description','location']
    ordering_fields = '__all__'


class NoticeViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for notice data'''
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title','caption','detail']
    ordering_fields = '__all__'



