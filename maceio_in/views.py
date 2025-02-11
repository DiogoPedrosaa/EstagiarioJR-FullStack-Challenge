from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from django.core.exceptions import ObjectDoesNotExist
from maceio_in.models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='post',
    request_body=RegisterSerializer,
    responses={201: openapi.Response("Usuário registrado com sucesso!"), 400: "Erro de validação"}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  
        return Response({"message": "Usuário foi registrado com sucesso!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='post',
    request_body=LoginSerializer,
    responses={200: openapi.Response("Login realizado com sucesso!"), 400: "Credenciais Incorretas"}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
   
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data)


    return Response({'error': 'Credenciais Incorretas'}, status=status.HTTP_400_BAD_REQUEST)




@swagger_auto_schema(
    method='post',
    responses={200: openapi.Response("Você foi deslogado com sucesso!")}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    return Response({'message': 'Você foi deslogado com sucesso.'}, status=status.HTTP_200_OK)



@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response("Lista de funcionários")}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def list_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=EmployeeSerializer,
    responses={201: openapi.Response("Funcionário criado com sucesso"), 400: "Erro de validação"}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='delete',
    responses={204: openapi.Response("Funcionário deletado com sucesso")}
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@swagger_auto_schema(
    method='put',
    request_body=EmployeeSerializer,
    responses={200: openapi.Response("Funcionário atualizado com sucesso"), 400: "Erro de validação"}
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response("Lista de setores")}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def list_departments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)



@swagger_auto_schema(
    method='post',
    request_body=DepartmentSerializer,
    responses={201: openapi.Response("Setor criado com sucesso"), 400: "Erro de validação"}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


