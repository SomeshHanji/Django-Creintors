from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Job,Applyjobs
from company.models import State,City


# Create job cards
def create_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        state = request.POST['state']
        city =request.POST['city']
        salary = request.POST['salary']
        exp_requried = request.POST['exp_requried']
        vacancy =request.POST['vacancy']
        description = request.POST['Description']
        selected_option = request.POST['options']
        
        # Get the State and City instances
        state = State.objects.get(id=state)
        city = City.objects.get(id=city)
        
        if title and description and state and city and exp_requried and vacancy and salary:
            job = Job(
                title=title,
                description=description,
                state=state,
                vacancy=vacancy,
                salary=salary,
                city=city,
                user=request.user,
                company=request.user.company,
                exp_requried=exp_requried,
            )
            job.save()  
            messages.info(request, 'New job has been created')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    states = State.objects.all()
    return render(request, 'job/create_job.html',{'states':states})

#update job card
def update_job(request, pk):
    if request.user.has_company:
        job = get_object_or_404(Job, id=pk)
        states = State.objects.all()
        cities=City.objects.all()
        
        if request.method == 'POST':
            title = request.POST['title']
            state_id = request.POST['state']
            city_id = request.POST['city']
            salary = request.POST['salary']
            vacancy = request.POST['vacancy']
            exp_requried=request.POST['exp_requried']
            description = request.POST['description']
            is_available = request.POST.get('options') == 'True'
            
            
            # Get the State and City instances
            state = State.objects.get(id=state_id)
            city = City.objects.get(id=city_id)
            
            if title and description and state and city and exp_requried and vacancy and salary:
                job.title = title
                job.state = state
                job.city = city
                job.salary = salary
                job.exp_requried = exp_requried
                job.vacancy = vacancy
                job.description = description
                job.is_available = is_available
                job.save()
                
                messages.info(request, 'Job has been updated')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Please fill in all required fields')
    else:
        messages.warnning(request,'Permission Denied')
        return render('dashboard') 
    job = get_object_or_404(Job, id=pk)
    states = State.objects.all()
    cities=City.objects.all() 
    return render(request, 'job/update_job.html', {'job': job,'cities':cities,'states': states})

#managing the jobs
def manage_jobs(request):
    jobs=Job.objects.filter(user=request.user,company=request.user.company)
    context={'jobs':jobs}
    return render(request,'job/manage_job.html',context)

#job application
def job_application(request,pk):
    if request.user.is_authenticated and request.user.is_applicant:
        job=Job.objects.get(pk=pk)
        if Applyjobs.objects.filter(user=request.user,job=pk).exists():
            messages.warning(request,'Permission Denied')
            return redirect('dashboard')
        else:
            Applyjobs.objects.create(
                job=job,
                user=request.user,
                status='Pending'
            )
            messages.info(request,'You have successfully applied..!please see the dashboard')
            return redirect('dashboard')
    else:
        messages.info(request,'You need to login for applying to the jobs')
        return redirect('login')

#view applications
def all_applicants(request,pk):
    job=Job.objects.get(pk=pk)
    applications=job.applyjobs_set.all()

    context={
        'job':job,
        'applications':applications
    }
    return render(request,'job/applicants.html',context)

def job_accepted(request,pk):
    if request.user.is_authenticated and request.user.is_recruiter:
        application = get_object_or_404(Applyjobs, pk=pk)
        user = application.user
        job=application.job
        application.status='Accepted'
        application.save()
        jobs = get_object_or_404(Job, title=job)
        context={
            'user':user,
            'jobs':jobs
        }
        return redirect('manage-jobs')
    messages.warning(request,'Permission Denied!,please login to continue.')
    return render('home')

def job_rejected(request,pk):
    if request.user.is_authenticated and request.user.is_recruiter:
        application = get_object_or_404(Applyjobs, pk=pk)
        user = application.user
        job=application.job
        application.status='Declined'
        application.save()
        jobs = get_object_or_404(Job, title=job)
        context={
            'user':user,
            'jobs':jobs
        }
        return redirect('manage-jobs')
    messages.warning(request,'Permission Denied!,please login to continue.')
    return render('home')

    # return render(request,"job/application_status_message.html",context) 

    # job=Applyjobs.objects.get(pk=pk)
    # job.status='Pending'
    # job.save()
    # return redirect('manage-jobs')

def view_applied_jobs(request):
    if request.user.is_applicant:
        applications=Applyjobs.objects.filter(user=request.user)
        return render(request,'users/jobs_applied.html',{'applications':applications})
    else:
        return render(request,'login')
    
def message_display(request,pk):
    application = get_object_or_404(Applyjobs, pk=pk)
    return render(request,'job/application_status_message.html',{'application':application})
    

