
from rest_framework import serializers
from .models import Designation, Employee

class DesignationSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for Designations data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Designation
        fields = ['id', 'title','short_name','org_unit','is_supervisory','employment_type','probation_period','employment_tenure','job_summary','job_description','headed_by','max_holders','salary_scale','supervisor']
        depth = 1
        
class EmployeeSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for Employees data'''
    class Meta:
        model = Employee
        fields = ['id','user','dob','designation','contract_duration','salutation','nationality','marital_status','employee_number','employment_type','probation_period','employment_tenure','salary_scale','joined_date','approved_by','file','village','is_approved','supervisor']
      