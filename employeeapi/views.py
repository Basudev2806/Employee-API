from django.db.models.query import QuerySet
from employeeapi.models import Employee
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmpSerializer


class EmpDetail(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    permission_classes = [permissions.IsAuthenticated]
