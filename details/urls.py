from django.urls import path, include
from rest_framework.routers import DefaultRouter

from details.views import EmployeeViewSet,DepartmentViewSet, LocationViewSet 

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)  
router.register(r'locations', LocationViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]