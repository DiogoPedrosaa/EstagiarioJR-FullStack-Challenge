from django.test import TestCase
from maceio_in.models import Department
from maceio_in.serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentSerializerTest(TestCase):
    def test_valid_department_serializer(self):
        data = {"name": "TI", "description": "Setor de Tecnologia da Informação"}
        serializer = DepartmentSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_department_serializer(self):
        data = {"description": "Setor de Tecnologia da Informação"}
        serializer = DepartmentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

class EmployeeSerializerTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="TI", description="Setor de Tecnologia da Informação")

    def test_valid_employee_serializer(self):
        data = {
            "name": "João Silva",
            "department": self.department.id,
            "email": "joao@gmail.com",
            "description": "Desenvolvedor Full Stack"
        }
        serializer = EmployeeSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_employee_serializer_missing_name(self):
        data = {
            "department": self.department.id,
            "email": "joao@gmail.com",
            "description": "Desenvolvedor Full Stack"
        }
        serializer = EmployeeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_invalid_employee_serializer_invalid_department(self):
        data = {
            "name": "João Silva",
            "department": 999,
            "email": "joao@gmail.com",
            "description": "Desenvolvedor Full Stack"
        }
        serializer = EmployeeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("department", serializer.errors)
