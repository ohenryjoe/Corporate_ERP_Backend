from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .serializers import *
from .models import *


# Create your views here.
class RegionViewSet(viewsets.ModelViewSet):
    queryset = region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class SubRegionViewSet(viewsets.ModelViewSet):
    queryset = sub_region.objects.all()
    serializer_class = SubRegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = district.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class LocalGovernmentViewSet(viewsets.ModelViewSet):
    queryset = local_government.objects.all()
    serializer_class = LocalGovernmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class CountyViewSet(viewsets.ModelViewSet):
    queryset = county.objects.all()
    serializer_class = CountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class SubCountyViewSet(viewsets.ModelViewSet):
    queryset = subcounty.objects.all()
    serializer_class = SubCountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class ParishViewSet(viewsets.ModelViewSet):
    queryset = parish.objects.all()
    serializer_class = ParishSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'


class VillageViewSet(viewsets.ModelViewSet):
    queryset = village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'
