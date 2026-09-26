from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    salary = models.FloatField()
    department= models.ForeignKey('Department', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.emp_name


class Department(models.Model):
    Department_id = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    location= models.ForeignKey('Location', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.DepartmentName

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city