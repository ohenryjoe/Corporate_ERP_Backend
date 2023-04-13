from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = region
        fields = ['id', 'code', 'name']
        # depth = 1
        
class SubRegionSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = sub_region
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = district
        fields = '__all__'

class LocalGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = local_government
        fields = '__all__'

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = county
        fields = '__all__'
        
class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = subcounty
        fields = '__all__'

class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = parish
        fields = '__all__'

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = village
        fields = '__all__'