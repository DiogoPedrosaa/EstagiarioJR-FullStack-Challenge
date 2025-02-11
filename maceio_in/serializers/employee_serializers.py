from rest_framework import serializers
from maceio_in.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'email', 'description']