from django.dispatch import receiver
from django.db.models.signals import pre_save
from accounts.views import get_random_string

from employee.models import Employee
from accounts.models import User, UserManager
from django.contrib.auth.hashers import make_password
from core.sendemail import new_user_created

@receiver(pre_save, sender=Employee)
def create_employee_user(sender, instance, *args, **kwargs):
    email = instance.email
    first_name = instance.othernames
    last_name = instance.surname
    pswd = make_password(get_random_string(8))
    employee = Employee.objects.filter(email=email).first()
    if not employee:
        User.objects.create(email=email, first_name=first_name,last_name=last_name,password=pswd)
        instance.user= User.objects.filter(email=email).first()
        new_user_created(instance)
    
   