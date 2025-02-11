from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from maceio_in.models import Department, Employee

class UserAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_register_user(self):
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/logout/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class EmployeeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="admin", password="admin")
        self.department = Department.objects.create(name="TI", description="Setor de Tecnologia da Informação")
        self.employee = Employee.objects.create(
            name="João Silva", department=self.department, email="joao@gmail.com", description="Dev"
        )

    def test_list_employees(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee(self):
        response = self.client.get(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "Maria Oliveira",
            "department": self.department.id,
            "email": "maria@gmail.com",
            "description": "Analista de Sistemas"
        }
        response = self.client.post("/api/employees/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_employee(self):
        self.client.force_authenticate(user=self.user)
        data = {"name": "João Silva Atualizado", "department": self.department.id, "email": "joao@gmail.com"}
        response = self.client.put(f"/api/employees/{self.employee.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/employees/delete/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DepartmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="admin", password="admin")
        self.department = Department.objects.create(name="Financeiro", description="Setor Financeiro")

    def test_list_departments(self):
        response = self.client.get("/api/departments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_department(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/api/departments/{self.department.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_department(self):
        self.client.force_authenticate(user=self.user)
        data = {"name": "RH", "description": "Recursos Humanos"}
        response = self.client.post("/api/departments/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_department(self):
        self.client.force_authenticate(user=self.user)
        data = {"name": "Financeiro Atualizado", "description": "Atualização"}
        response = self.client.patch(f"/api/departments/{self.department.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_department(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/departments/delete/{self.department.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
