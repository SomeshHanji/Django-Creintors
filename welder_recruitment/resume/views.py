from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Resume
from users.models import User

# Create your views here.
def update_resume(request):
    if request.user.is_applicant:
        try:
            resume = Resume.objects.get(user=request.user)
            # Check if the company instance is "empty"
            if not resume.first_name and not resume.surname and not resume.location and not resume.job_title:
                resume = None
        except Resume.DoesNotExist:
            resume = None
        if request.method == 'POST':
            user = User.objects.get(id=request.user.id)
            userid=user.id
            name = request.POST['name']
            surname = request.POST['surname']
            location = request.POST['city']
            job_title = request.POST['job_title']
            var = Resume.objects.create(user=user, first_name=name, surname=surname, location=location, job_title=job_title)
            user.has_resume=True
            user.save()
            var.save()
            messages.info(request,'your resume information  has been updated!')
            return redirect('dashboard')
        return render(request, 'resume/update_resume.html')
    else:
        messages.warning(request,'Permission Denied')
        return redirect('dashboard')
    
#view profile/resume
def resume_details(request,pk):
    resume=Resume.objects.get(pk=pk)
    context={'resume':resume}
    return render(request,'resume/resume_details.html',context)