from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcripts, name="transcripts"),
    path('transcript/<str:pk>/', views.transcript, name="transcript"),
]