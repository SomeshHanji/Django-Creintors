from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
    path('update-resume/', views.update_resume , name='update-resume'),
    path('resume-details/<int:pk>', views.resume_details , name='resume-details'),
]