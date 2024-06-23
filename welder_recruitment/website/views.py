from django.shortcuts import render
from job.models import Applyjobs, Job
from .filter import JobFilter


#rendering the home page
def home(request):
    filter=JobFilter(request.GET,queryset=Job.objects.filter().order_by('-timestamp'))
    context={'filter':filter}
    return render(request,'website/home.html',context)


#listing job offers
def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context={'jobs':jobs}
    return render(request,'website/job_listing.html',context)

#job details
def job_details(request,pk):
    has_applied=False
    if request.user.is_authenticated:
        if Applyjobs.objects.filter(user=request.user,job=pk).exists():
            has_applied=True
        else:
            has_applied=False
    job=Job.objects.get(pk=pk)
    context = {'job':job,'has_applied':has_applied}
    return render(request,'website/job_details.html',context)
 
