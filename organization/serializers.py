from rest_framework import serializers
from .models import SalaryScale, CorporateEntity, Unit, Event, Notice



class SalaryScaleSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for salary scale data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = SalaryScale
        fields = ['id', 'scale','rank_order','title','rank_description']


class CorporateEntitySerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for corporate entity data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = CorporateEntity
        fields = ['id', 'rank','title','description','headed_by']


class UnitSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for unit data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Unit
        fields = ['id', 'title','entity','parent_entity','parent_unit','description']


class EventSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for event data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Event
        fields = ['id', 'title','caption','description','start_datetime','end_datetime','location','attachment']


class NoticeSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for notice data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Notice
        fields = ['id', 'title','event','caption','detail','date_published','attachment']