from rest_framework import serializers
from .models import Nationality

class NationalitySerializer(serializers.ModelSerializer):
    '''manage crud operations for Nationality data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Nationality
        fields = ['id', 'name']

