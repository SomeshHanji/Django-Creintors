from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
    path('update-company/', views.update_company , name='update-company'),
    path('company-details/<int:pk>', views.company_details , name='company-details'),
    
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]