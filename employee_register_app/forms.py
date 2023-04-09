from django import forms
from .models import Employee




class employeeForm(forms.ModelForm):
    class Meta:
            model=Employee
            fields='__all__'
            labels={
               'full_name' :'Full Name' ,
               'emp_code' :'EMP. Code' ,
            }
