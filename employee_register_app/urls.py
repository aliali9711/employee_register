



from django.urls import path, re_path
from . import views



urlpatterns = [
   path("",views.home ,name="employee") ,
   path("list/",views.employee_list ,name="employee") 
]