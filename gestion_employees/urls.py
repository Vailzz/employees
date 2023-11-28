from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('View_Employees/', views.employeeCreateView.as_view),
]
