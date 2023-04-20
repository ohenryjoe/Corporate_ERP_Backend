from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .models import AppraisalFrequency,AppraisalPerformanceFactor,AppraisalSchedule,AppraiseePerformanceIndicator,Appraisal,PerformanceImprovementPlan
from .serializers import (AppraisalFrequencySerializer,AppraisalPerformanceFactorSerializer,AppraisalScheduleSerializer, AppraiseePerformanceIndicatorSerializer,AppraisalSerializer,PerformanceImprovementPlanSerializer)
# Create your views here.

class AppraisalFrequencyViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Appraisal Frequency data'''
    queryset = AppraisalFrequency.objects.all()
    serializer_class = AppraisalFrequencySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title','duration']
    ordering_fields = '__all__'


class AppraisalPerformanceFactorViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Appraisal Performance Factor data'''
    queryset = AppraisalPerformanceFactor.objects.all()
    serializer_class = AppraisalPerformanceFactorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title','description','scores']
    ordering_fields = '__all__'


class AppraisalScheduleViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Appraisal Performance Factor data'''
    queryset = AppraisalSchedule.objects.all()
    serializer_class = AppraisalScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['frequency__title','appraisee__first_name','appraisee__last_name','appraiser__first_name']
    ordering_fields = '__all__'


class AppraiseePerformanceIndicatorViewSet(viewsets.ModelViewSet):
    '''Endpoint to manage crud operations for Appraisal Performance Factor data'''
    queryset = AppraiseePerformanceIndicator.objects.all()
    serializer_class = AppraiseePerformanceIndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['frequency__title','appraisee__first_name','appraisee__last_name','appraiser__first_name']
    ordering_fields = '__all__'