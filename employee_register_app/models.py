from django.db import models

class Position(models.Model):
     title=models.CharField(max_length=50)
     def __str__ (self):
          return f"{self.title}"

    



class Employee(models.Model):
    full_name=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    position=models.ForeignKey(Position, related_name="pos_emp", on_delete=models.CASCADE)
