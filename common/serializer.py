from rest_framework import serializers
from .models import Nationality, Region, SubRegion, District, LocalGovernment, County, SubCounty, Parish, Village

class NationalitySerializer(serializers.ModelSerializer):
    '''manage crud operations for Nationality data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Nationality
        fields = ['id', 'name']

class RegionSerializer(serializers.ModelSerializer):
    '''manage crud operations for Region data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Region
        fields = ['id', 'name','code','active']

class SubRegionSerializer(serializers.ModelSerializer):
    '''manage crud operations for SubRegion data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = SubRegion
        fields = ['id', 'name','code','region']


class DistrictSerializer(serializers.ModelSerializer):
    '''manage crud operations for District data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = District
        fields = ['id', 'name','code','sub_region','active']

class LocalGovernmentSerializer(serializers.ModelSerializer):
    '''manage crud operations for Local Governments data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = LocalGovernment
        fields = ['id', 'name','vote_code','district','active']

class CountySerializer(serializers.ModelSerializer):
    '''manage crud operations for Local County data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = County
        fields = ['id', 'district','local_gov','code','name','constituency']

class SubCountySerializer(serializers.ModelSerializer):
    '''manage crud operations for SubCounty data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = SubCounty
        fields = ['id', 'name','code','county','active']


class ParishSerializer(serializers.ModelSerializer):
    '''manage crud operations for Parish data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Parish
        fields = ['id', 'name','code','subcounty','postcode','active']



class VillageSerializer(serializers.ModelSerializer):
    '''manage crud operations for village data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Village
        fields = ['id', 'name','code','parish','active']