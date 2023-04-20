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

    def to_representation(self, instance):
        rep = super(SubRegionSerializer, self).to_representation(instance)
        rep['region'] = instance.region.name
        return rep


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = district
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(DistrictSerializer, self).to_representation(instance)
        rep['sub_region'] = instance.sub_region.name
        return rep


class LocalGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = local_government
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(LocalGovernmentSerializer, self).to_representation(instance)
        rep['district'] = instance.district.name
        return rep


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = county
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(CountySerializer, self).to_representation(instance)
        rep['district'] = instance.district.name
        rep['local_gov'] = instance.local_gov.name
        return rep


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = subcounty
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(SubCountySerializer, self).to_representation(instance)
        rep['county'] = instance.county.name
        return rep


class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = parish
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(ParishSerializer, self).to_representation(instance)
        rep['subcounty'] = instance.subcounty.name
        return rep


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = village
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(VillageSerializer, self).to_representation(instance)
        rep['parish'] = instance.parish.name
        return rep
