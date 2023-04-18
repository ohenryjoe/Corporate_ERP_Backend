from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .serializers import DesignationSerializer, EmployeeSerializer, BankingSerializer, ExperienceSerializer, \
    EducationSerializer, RelatedPersonSerializer, AddressSerializer, ContactSerializer, AppointmentSerializer
from .models import Designation, Employee, Banking, Experience, Education, RelatedPerson, Address, Contact, Appointment


# Create your views here.
class DesignationViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud operations for Designation data'''
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['title', 'short_name', 'job_summary', 'job_description', ]
    ordering_fields = '__all__'


class EmployeeViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud  for employee data'''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['surname', 'othernames', 'employeeNumber']
    ordering_fields = '__all__'


class AppointmentViewSet(viewsets.ModelViewSet):
    '''Viewset to manage crud  for employee data'''
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['start_date', 'end_date', 'designation', 'employee']
    ordering_fields = '__all__'


class BankingViewSet(viewsets.ModelViewSet):
    queryset = Banking.objects.all()
    serializer_class = BankingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['accountName', 'bankName', 'accountNumber', ]
    ordering_fields = '__all__'


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['org_name', 'job_title', 'employee_surname', 'employee_othernames']
    ordering_fields = '__all__'


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['institution_name', 'job_title', 'employee_surname', 'employee_othernames', 'qualification_title']
    ordering_fields = '__all__'


class RelatedPersonViewSet(viewsets.ModelViewSet):
    queryset = RelatedPerson.objects.all()
    serializer_class = RelatedPersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['employee_othernames', 'employee_surname', 'full_name', 'gender', 'date_of_birth', 'nin',
                     'relationship', 'is_nok', 'is_dependant', 'email', 'mobile', 'address']
    ordering_fields = '__all__'


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['employee', 'region', 'district', 'county', 'subcounty', 'parish', 'village']
    ordering_fields = '__all__'


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None
    search_fields = ['employee_surname', 'employee_othernames', 'email', 'phone']
    ordering_fields = '__all__'
