from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('register-applicant/',views.register_applicant,name='register-applicant'),
    path('register-recruiter/',views.register_recruiter,name='register-recruiter'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('applicant-profile/<int:pk>/',views.recruite_profile_view,name='applicant-profile'),
    path('',views.index,name='index'),
]