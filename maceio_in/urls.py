from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('employees/', views.list_employees, name='list_employees'),
    path('employees/<int:pk>/', views.get_employee, name='get_employee'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/update/<int:pk>/', views.update_employee, name='update_employee'),
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('departments/', views.list_departments, name='list_departments'),
    path('departments/<int:pk>/', views.get_department, name='get_department'),
    path('departments/create/', views.create_department, name='create_department'),
    path('departments/update/<int:pk>/', views.update_department, name='update_department'),
    path('departments/delete/<int:pk>/', views.delete_department, name='delete_department'),
]