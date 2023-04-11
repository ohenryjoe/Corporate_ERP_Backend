from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializer import (NationalitySerializer, RegionSerializer, SubRegionSerializer, DistrictSerializer,
                        LocalGovernmentSerializer,CountySerializer, SubCountySerializer, ParishSerializer, VillageSerializer)
from .models import Nationality,Region,SubRegion,District,LocalGovernment,County,SubCounty,Parish,Village

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


class RegionViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Regions data'''
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','code']
    ordering_fields = '__all__'


class SubRegionViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Sub Regions data'''
    queryset = SubRegion.objects.all()
    serializer_class = SubRegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','code','region__name']
    ordering_fields = '__all__'



class DistrictViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Districts data'''
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','code','sub_region__name']
    ordering_fields = '__all__'



class LocalGovernmentViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for LocalGovernments data'''
    queryset = LocalGovernment.objects.all()
    serializer_class = LocalGovernmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','district__name','vote_code']
    ordering_fields = '__all__'


class CountyViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Counties data'''
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','district__name','local_gov__name','code','constituency']
    ordering_fields = '__all__'

class SubCountyViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Sub Counties data'''
    queryset = SubCounty.objects.all()
    serializer_class = SubCountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','county__name','code']
    ordering_fields = '__all__'


class ParishViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Parishes data'''
    queryset = Parish.objects.all()
    serializer_class = ParishSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','subcounty__name','code','postcode']
    ordering_fields = '__all__'

class VillageViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for villages data'''
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name','parish__name','code']
    ordering_fields = '__all__'