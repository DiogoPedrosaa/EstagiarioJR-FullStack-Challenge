from django.test import TestCase
from maceio_in.models import Department, Employee

class DepartmentModelTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(
            name='RH',
            description='Setor responsável pela gestão de pessoas'
        )

    def test_department_creation(self):
        self.assertEqual(self.department.name, 'RH')
        self.assertEqual(self.department.description, 'Setor responsável pela gestão de pessoas')

    def test_department_str(self):
        self.assertEqual(str(self.department), 'RH')


class EmployeeModelTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(
            name='TI',
            description='Departamento responsável pela infraestrutura e tecnologias da secretaria'
        )
        self.employee = Employee.objects.create(
            name='João Silva',
            department=self.department,
            email='joao.silva@gmail.com',
            description='Desenvolvedor Backend'
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, 'João Silva')
        self.assertEqual(self.employee.department.name, 'TI')
        self.assertEqual(self.employee.email, 'joao.silva@gmail.com')
        self.assertEqual(self.employee.description, 'Desenvolvedor Backend')

    def test_employee_str(self):
        self.assertEqual(str(self.employee), 'João Silva')