from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name="students-list"),
    path('student/<str:pk>/', views.student, name='student'),
    path('create-student/', views.create_student, name="create-student"),
    path('update-student/<str:pk>/', views.update_student_detail, name="update-student"),
    path('delete-student/<str:pk>/', views.delete_student, name="delete-student"),
]