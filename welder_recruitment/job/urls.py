from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('create-job/', views.create_job ,name='create-job'),  
    path('update-job/<int:pk>/', views.update_job ,name='update-job'),
    path('manage-jobs/',views.manage_jobs,name='manage-jobs'),
    path('job-application/<int:pk>/',views.job_application,name='job-application'),
    path('applicants/<int:pk>/',views.all_applicants,name='applicants'),
    path('accepted/<int:pk>/',views.job_accepted,name='accepted'),
    path('declined/<int:pk>/',views.job_rejected,name='declined'),
    path('jobs-applied/',views.view_applied_jobs,name='jobs-applied'),
    path('message/<int:pk>/',views.message_display,name='message')
]