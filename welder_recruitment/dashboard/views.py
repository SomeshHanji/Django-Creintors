from django.db.models import Count
from django.shortcuts import render,redirect
from company.models import Company
from job.models import Job,Applyjobs
from resume.models import Resume

def dashboard(request):
    jobs_count = Job.objects.filter(user=request.user).count()  
    companies = Company.objects.annotate(applications_count=Count('job__applyjobs'))
    accepted_applications = Applyjobs.objects.filter(status='Accepted')[:3]
        
        # Get users' profile pictures and job salaries
    data = []
    for application in accepted_applications:
        user_profile = Resume.objects.get(user=application.user)
        data.append({
                'profile_picture': user_profile.profile_photo.url,
                'job_salary': application.job.salary
            })
    context = {
        'jobs_count': jobs_count,
        'companies': companies,
        'data':data
    }
    return render(request, 'dashboard/dashboard.html', context)