from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='Sem Descrição', blank=True, null=True)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.TextField(default='Sem Descrição', blank=True, null=True)

    def __str__(self):
        return self.name