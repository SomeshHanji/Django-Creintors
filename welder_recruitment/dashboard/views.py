from django.db.models import Count
from django.shortcuts import render,redirect
from company.models import Company
from job.models import Job,Applyjobs

def dashboard(request):
    jobs_count = Job.objects.filter(user=request.user).count()  
    companies = Company.objects.annotate(applications_count=Count('job__applyjobs'))
    context = {
        'jobs_count': jobs_count,
        'companies': companies,
    }
    return render(request, 'dashboard/dashboard.html', context)