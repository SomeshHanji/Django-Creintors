from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('create-job/', views.create_job ,name='create-job'),  
    path('update-job/', views.update_job ,name='update-job'),
    path('manage-jobs/',views.manage_jobs,name='manage-jobs'),
    path('job-application/<int:pk>/',views.job_application,name='job-application'),
    path('applicants/<int:pk>/',views.all_applicants,name='applicants')
]