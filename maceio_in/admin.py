from django.contrib import admin
from .models import Department, Employee

#Aqui eu registrei os models para fazer testes no painel admin do Django.
admin.site.register(Department)
admin.site.register(Employee)

