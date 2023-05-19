from rest_framework import viewsets, permissions, filters
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
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

    def create(self, request, format=None):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = serializer.validated_data['name']

                region_obj = region.objects.filter(name=name).first()
                print(region_obj, 'This is the region object')
                if not region_obj:
                    user = self.request.user
                    serializer.save(created_by=user)
            except IntegrityError:
                return Response({'error': 'Region already exists'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubRegionViewSet(viewsets.ModelViewSet):
    queryset = sub_region.objects.all()
    serializer_class = SubRegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = sub_region.objects.all()
        region_id = self.request.query_params.get('region_code', None)
       
        if region_id is not None:
            queryset = queryset.filter(code=region_id)
        return queryset

    def create(self, request, format=None):
        serializer = SubRegionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = serializer.validated_data['name']

                region_obj = sub_region.objects.filter(name=name).first()
            
                if not region_obj:
                    user = self.request.user
                    serializer.save(created_by=user)
            except IntegrityError:
                return Response({'error': 'Sub-region already exists'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = district.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = district.objects.all()
        sub_region_id = self.request.query_params.get('sub_region_id', None)
    
        if sub_region_id is not None:
            queryset = queryset.filter(sub_region_id=sub_region_id)
        return queryset
    
    def create(self, request, format=None):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = serializer.validated_data['name']

                region_obj = district.objects.filter(name=name).first()
            
                if not region_obj:
                    user = self.request.user
                    serializer.save(created_by=user)
            except IntegrityError:
                return Response({'error': 'District already exists'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class LocalGovernmentViewSet(viewsets.ModelViewSet):
    queryset = local_government.objects.all()
    serializer_class = LocalGovernmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = local_government.objects.all()
        district_id = self.request.query_params.get('district_id', None)
        if district_id is not None:
            queryset = queryset.filter(district_id=district_id)
        return queryset
    
    def create(self, request, format=None):
        serializer = LocalGovernmentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = serializer.validated_data['name']

                region_obj = local_government.objects.filter(name=name).first()
            
                if not region_obj:
                    user = self.request.user
                    serializer.save(created_by=user)
            except IntegrityError:
                return Response({'error': 'Sub-region already exists'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountyViewSet(viewsets.ModelViewSet):
    queryset = county.objects.all()
    serializer_class = CountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = county.objects.all()
        district_id = self.request.query_params.get('district_id', None)
        if district_id is not None:
            queryset = queryset.filter(district_id=district_id)
        return queryset


class SubCountyViewSet(viewsets.ModelViewSet):
    queryset = subcounty.objects.all()
    serializer_class = SubCountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = subcounty.objects.all()
        county_id = self.request.query_params.get('county_id', None)
        if county_id is not None:
            queryset = queryset.filter(county_id=county_id)
        return queryset


class ParishViewSet(viewsets.ModelViewSet):
    queryset = parish.objects.all()
    serializer_class = ParishSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = parish.objects.all()
        subcounty_id = self.request.query_params.get('subcounty_id', None)
        if subcounty_id is not None:
            queryset = queryset.filter(subcounty_id=subcounty_id)
        return queryset


class VillageViewSet(viewsets.ModelViewSet):
    queryset = village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = village.objects.all()
        parish_id = self.request.query_params.get('parish_id', None)
        if parish_id is not None:
            queryset = queryset.filter(parish_id=parish_id)
        return queryset
