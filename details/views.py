from .models import Employee,Department,Location
from .serializers import EmployeeSerializer,DepartmentSerializer,LocationSerializer,EmployeeCombinedSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'message': 'Employee created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    
    def list(self, request):

        employeeName = request.query_params.get('employee_name', None)
        employeeid = request.query_params.get('employee_id', None)
        departmentid = request.query_params.get('department_id', None)
        locationid = request.query_params.get('location_id', None)
        salary = request.query_params.get('salary', None)

        if employeeName:
            employeeData = Employee.objects.filter(
            emp_name__icontains=employeeName
    )
        elif employeeid:
            employeeData = Employee.objects.filter(
            emp_id=employeeid
    )
        elif departmentid:
            employeeData = Employee.objects.filter(
            department__Department_id=departmentid
    )
        elif locationid:
            employeeData = Employee.objects.filter(
            department__location__location_id=locationid
    )

        elif salary:
            employeeData = Employee.objects.filter(
            salary__gte=salary
    )   
        else:
           employeeData = Employee.objects.all()
        serializer = EmployeeCombinedSerializer(employeeData, many=True)

        return Response(
            {
                'employees_count': employeeData.count(),
                'message': 'Employees retrieved successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

    
    def destroy(self, request, pk=None):

        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()

            return Response(
                {
                    'message': 'Employee deleted successfully'
                },
                status=status.HTTP_200_OK
            )

        except Employee.DoesNotExist:

            return Response(
                {
                    'message': 'Employee not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    
    def update(self, request, pk=None):


        try:
            employee = Employee.objects.get(pk=pk)

            serializer = EmployeeSerializer(
                employee,
                data=request.data
            )

            if serializer.is_valid():
                serializer.save()

                return Response(
                    {
                        'message': 'Employee updated successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Employee.DoesNotExist:

            return Response(
                {
                    'message': 'Employee not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)

            serializer = EmployeeCombinedSerializer(employee)

            return Response(
            {
                'message': 'Employee retrieved successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

        except Employee.DoesNotExist:
             

            return Response(
            {
                'message': 'Employee not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def create(self, request):

        serializer = DepartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'message': 'Department created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request):

        depart_Name = request.query_params.get('department_name', None)
        depart_id = request.query_params.get('department_id', None)

        if depart_Name:
            departmentData = Department.objects.filter(
                DepartmentName__icontains=depart_Name
            )

        elif depart_id:
            departmentData = Department.objects.filter(
                Department_id=depart_id
            )

        else:
            departmentData = Department.objects.all()

        serializer = DepartmentSerializer(
            departmentData,
            many=True
        )

        return Response(
            {
                'departments_count': departmentData.count(),
                'message': 'Departments retrieved successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):

        try:
            department = Department.objects.get(pk=pk)
            department.delete()

            return Response(
                {
                    'message': 'Department deleted successfully'
                },
                status=status.HTTP_200_OK
            )

        except Department.DoesNotExist:

            return Response(
                {
                    'message': 'Department not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):

        try:
            department = Department.objects.get(pk=pk)

            serializer = DepartmentSerializer(
                department,
                data=request.data
            )

            if serializer.is_valid():
                serializer.save()

                return Response(
                    {
                        'message': 'Department updated successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Department.DoesNotExist:

            return Response(
                {
                    'message': 'Department not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


    def create(self, request):
                
                serializer = LocationSerializer(data=request.data)
        
                if serializer.is_valid():
                    serializer.save()
        
                    return Response(
                        {
                            'message': 'Location created successfully',
                            'data': serializer.data
                        },
                        status=status.HTTP_201_CREATED
                    )
        
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
    def list(self, request):
        
                city = request.query_params.get('city', None)
                location_id = request.query_params.get('location_id', None)
        
                if city:
                    locationData = Location.objects.filter(
                        city__icontains=city
                    )
        
                elif location_id:
                    locationData = Location.objects.filter(
                        location_id=location_id
                    )
        
                else:
                    locationData = Location.objects.all()
        
                serializer = LocationSerializer(locationData, many=True)
        
                return Response(
                    {
                        'locations_count': locationData.count(),
                        'message': 'Locations retrieved successfully',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK
                )
    def destroy(self, request, pk=None):
        
                try:
                    location = Location.objects.get(pk=pk)
                    location.delete()
        
                    return Response(
                        {
                            'message': 'Location deleted successfully'
                        },
                        status=status.HTTP_200_OK
                    )
        
                except Location.DoesNotExist:
        
                    return Response(
                        {
                            'message': 'Location not found'
                        },
                        status=status.HTTP_404_NOT_FOUND
                    )

    def update(self, request, pk=None):
        
        
                try:
                    location = Location.objects.get(pk=pk)
        
                    serializer = LocationSerializer(
                        location,
                        data=request.data
                    )
        
                    if serializer.is_valid():
                        serializer.save()
        
                        return Response(
                            {
                                'message': 'Location updated successfully',
                                'data': serializer.data
                            },
                            status=status.HTTP_200_OK
                        )
        
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                    )
        
                except Location.DoesNotExist:
        
                    return Response(
                        {
                            'message': 'Location not found'
                        },
                        status=status.HTTP_404_NOT_FOUND
                    )
    