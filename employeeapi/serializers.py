from django.db.models import fields
from rest_framework import serializers
from employeeapi.models import Employee

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['EID','Name','Salary']