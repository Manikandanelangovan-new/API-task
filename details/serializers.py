from rest_framework import serializers
from .models import Department, Employee, Location

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class EmployeeCombinedSerializer(serializers.ModelSerializer):
    
    Employee_id = serializers.IntegerField(source='emp_id')
    fullName = serializers.CharField(source='emp_name')
    department_id = serializers.IntegerField(source='department.Department_id')
    Department_id = serializers.IntegerField(source='department.Department_id')
    departmentName = serializers.CharField(source='department.DepartmentName')
    location_id = serializers.IntegerField(source='department.location.location_id')
    Location_id = serializers.IntegerField(source='department.location.location_id')
    city = serializers.CharField(source='department.location.city')

    class Meta:
        model = Employee
        fields = [
            'Employee_id',
            'fullName',
            'salary',
            'department_id',
            'Department_id',
            'departmentName',
            'location_id',
            'Location_id',
            'city'
        ]