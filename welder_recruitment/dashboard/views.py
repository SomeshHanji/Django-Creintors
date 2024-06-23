from django.db.models import Count
from django.shortcuts import render,redirect
from company.models import Company
from job.models import Job,Applyjobs

def dashboard(request):
    # Count the number of jobs posted by the current user
    jobs_count = Job.objects.filter(user=request.user).count()
    
    # Annotate each company with the count of applications received for their jobs
    companies = Company.objects.annotate(applications_count=Count('job__applyjobs'))
    
    context = {
        'jobs_count': jobs_count,
        'companies': companies,
    }
    return render(request, 'dashboard/dashboard.html', context)