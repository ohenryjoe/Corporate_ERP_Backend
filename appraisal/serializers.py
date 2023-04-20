from rest_framework import serializers
from .models import AppraisalFrequency,AppraisalPerformanceFactor,AppraisalSchedule,AppraiseePerformanceIndicator,Appraisal,PerformanceImprovementPlan



class AppraisalFrequencySerializer(serializers.ModelSerializer):
    '''manage crud operations for Appraisal Frequency data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = AppraisalFrequency
        fields = ['id', 'title','duration','is_for_probational','is_adhoc']


class AppraisalPerformanceFactorSerializer(serializers.ModelSerializer):
    '''manage crud operations for Appraisal Performance Factor data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = AppraisalPerformanceFactor
        fields = ['id', 'title','description','scores','created_by']

    



class AppraisalScheduleSerializer(serializers.ModelSerializer):
    '''manage crud operations for Appraisal  Schedule data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = AppraisalSchedule
        fields = ['id', 'frequency','appraisee','appraiser','start_date','end_date','appraisal_opened_at','appraisal_deadline_date','status']
    def to_representation(self, instance):
        rep = super(AppraisalScheduleSerializer, self).to_representation(instance)
        rep['frequency'] = instance.frequency.title
        rep['appraisee'] = instance.appraisee.email
        rep['appraiser'] = instance.appraisee.email
        return rep

class AppraiseePerformanceIndicatorSerializer(serializers.ModelSerializer):
    '''manage crud operations for Appraisee Performance Indicator data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = AppraiseePerformanceIndicator
        fields = ['id', 'appraisal_schedule','performance_indicators','is_active']



class AppraisalSerializer(serializers.ModelSerializer):
    '''manage crud operations for Appraisal data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Appraisal
        fields = ['id', 'schedule','self_reviewed_at','supervisor_reviewed_at','supervisor_pffs_reviewed_at','completed_at','KRA_data',
                  'KRA_total_score','KRA_total_obtained_score','KRA_total_percentage','PFSS_data','PFSS_total_percentage','total_percentage']
        
class PerformanceImprovementPlanSerializer(serializers.ModelSerializer):
    '''manage crud operations for Performance Improvement Plan data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = PerformanceImprovementPlan
        fields = ['id', 'appraisal_schedule','data']
