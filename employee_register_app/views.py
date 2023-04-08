from django.shortcuts import render

from .forms import employeeForm



def employee_list (request):
    return  render(request,'employee_register_app\employee_list.html')

def employee_form (request):
    form=employeeForm()
    content={
        'form':form
    }
    return  render(request,'employee_register_app\employee_form.html', content)

def employee_delete (request):
    return()