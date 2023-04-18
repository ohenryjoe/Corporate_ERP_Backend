from rest_framework import serializers
from .models import LeaveType,LeavePolicy, LeaveBalance, LeaveRequest,LeaveRequestStage, Leave, LeaveProcessManager



class LeaveTypeSerializer(serializers.ModelSerializer):
    '''manage crud operations for leave type data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = LeaveType
        fields = ['id', 'name','description']


    

class LeavePolicySerializer(serializers.ModelSerializer):
    '''manage crud operations for Leave Policy  data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = LeavePolicy
        fields = ['id', 'leave_type','name','description','is_paid','must_be_earned',
                  'earned_after','is_carry_forward','total_days','minimum_days','is_active',
                  'gender','salary_scales']
        


class LeaveBalanceSerializer(serializers.ModelSerializer):
    '''manage crud operations for Leave Policy  data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = LeaveBalance
        fields = ['id', 'employee','leave_policy','days_taken','current_balance','upcoming_balance_update_date']


class LeaveRequestSerializer(serializers.ModelSerializer):
    '''manage crid operations for leave request'''

    class Meta:
        '''Meta data to define the model and fields to be serialized'''
        model = LeaveRequest
        fields = ['id','employee','leave_policy','leave_balance','start_date','end_date','status','recipient','remarks']


class LeaveRequestStageSerializer(serializers.ModelSerializer):
    '''manage crid operations for leave request stage'''

    class Meta:
        '''Meta data to define the model and fields to be serialized'''
        model = LeaveRequestStage
        fields = ['id','leave_request','actor','start_date','end_date','action','forwarded_to','remarks','is_completed']


class LeaveSerializer(serializers.ModelSerializer):
    '''manage crud operations for leave'''

    class Meta:
        '''Meta data to define the model and fields to be serialized'''
        model = Leave
        fields = ['id','request','start_date','end_date']


class LeaveProcessManagerSerializer(serializers.ModelSerializer):
    '''manage crud operations for leave process manager'''
    class Meta:
        '''Meta definition of model class and fields to be serialized'''
        model = LeaveProcessManager
        fields =  ['id','employee','leave_process','assigned_to']