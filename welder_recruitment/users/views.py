from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from job.models import Applyjobs, Job
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company

# registered applicant only.
def register_applicant(request):
    if request.method == 'POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)   
            var.is_applicant=True
            var.username=var.email
            var.save() 
            Company.objects.create(user=var)

            messages.info(request,'Your account is created.')
            return redirect('login') 
        else:
            messages.warning(request,'Somthing went Wrong')
            return redirect('register-applicant') 
    else:
        form = RegisterUserForm()
        context={'form':form}
        return render(request,'users/register_applicant.html',context)



#register recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)   
            var.is_recruiter=True
            var.username=var.email
            var.save() 
            Resume.objects.create(user=var)

            messages.info(request,'Your account is created.')
            return redirect('login') 
        else:
            messages.warning(request,'Somthing went Wrong')
            return redirect('register-recruiter') 
    else:
        form = RegisterUserForm()
        context={'form':form}
        return render(request,'users/register_recruiter.html',context)


    
#login a user
def login_user(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(request,username=email, password=password)
        
        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard')
            
        else:
            messages.warning(request,'something went wrong try again..!')
            return redirect('login')
    else:
        return render(request,'users/login.html')


    
#logout user
def logout_user(request):
    logout(request)
    messages.info(request,'your are logged out')
    return redirect('login')

def index(request):
    return render(request, "users/base.html")

def profile(request):
    resume = get_object_or_404(Resume, user=request.user) 
    email = request.user
    context={'resume':resume,'email':email}
    return render(request,"users/profile.html",context)

def recruite_profile_view(request,pk):
    application = get_object_or_404(Applyjobs, id=pk)
    user = application.user
    resume = get_object_or_404(Resume, user=user)
    context={'resume':resume}
    
    return render(request,"users/profile.html",context)

def application_status_update(request,pk):
    application = get_object_or_404(Applyjobs, id=pk)
    user = application.user
    job=application.job
    jobs = get_object_or_404(jobs, job=job)
    context={
        'user':user,
        'jobs':jobs
    }
    return render(request,"job/application_status_message",context)


