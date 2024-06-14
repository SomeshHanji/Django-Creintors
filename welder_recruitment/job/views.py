from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Job,Applyjobs


# Create job cards
def create_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        salary = request.POST['salary']
        requiements = request.POST['Requirements']
        description = request.POST['Description']
        
        if title and description and location and salary and requiements:
            job = Job(
                title=title,
                description=description,
                location=location,
                salary=salary,
                user=request.user,
                company=request.user.company,
                requirements=requiements,
            )
            job.save()  
            messages.info(request, 'New job has been created')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    return render(request, 'job/create_job.html')

#update job card
def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        salary = request.POST['salary']
        requiement = request.POST['requirements']

        if title and description and location and salary:
            job.title = title
            job.description = description
            job.location = location
            job.salary = salary
            job.requirements=requiement
            job.save()
            
            messages.info(request, 'Your job info is updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')

    return render(request, 'job/update_job.html', {'job': job})

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
   