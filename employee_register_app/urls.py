



from django.urls import path, re_path
from . import views



urlpatterns = [
   
   path("list/",views.employee_list ,name="employee_list") ,
   path("form/",views.employee_form ,name="employee_form") ,
]