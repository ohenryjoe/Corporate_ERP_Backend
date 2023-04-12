
from rest_framework import serializers
from .models import Designation, Employee, Banking, Experience, Education, RelatedPerson, Address, Contact

class DesignationSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for Designations data'''
    class Meta:
        '''Meta class to define the model and fields to be serialized'''
        model = Designation
        fields = ['id', 'title','short_name','org_unit','is_supervisory','employment_type','probation_period','employment_tenure','job_summary','job_description','headed_by','max_holders','salary_scale','supervisor']
        # depth = 1
        
class EmployeeSerializer(serializers.ModelSerializer):
    '''Serializer to manage crud operations for Employees data'''
    class Meta:
        model = Employee
        fields = ['id','user', 'surname', 'othernames', 'dob', 'salutation', 'nationality', 'marital_status', 'profilePic', 'phone1', 'phone2', 'religion']

class BankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banking
        fields = ['id', 'employee', 'accountName', 'accountNumber', 'bankName']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'employee', 'job_title', 'org_name', 'org_website', 'org_telephone', 'org_email', 'description', 'from_date', 'to_date']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'employee', 'qualification_title', 'qualification_title', 'institution_name', 'institution_website', 'institution_address', 'institution_email', 'qualification_description', 'start_date', 'end_date', 'graduation_date']

class RelatedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedPerson
        fields = ['id', 'employee', 'full_name', 'gender', 'date_of_birth', 'nin', 'relationship', 'is_nok', 'is_dependant', 'email', 'mobile', 'address']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'employee', 'region', 'district', 'county', 'subcounty', 'parish', 'village']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'employee', 'email', 'phone']