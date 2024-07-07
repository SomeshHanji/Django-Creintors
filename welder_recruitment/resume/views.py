from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Resume
from users.models import User
from company.models import City

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
            name = request.POST['name']
            surname = request.POST['surname']
            location = request.POST['city']
            job_title = request.POST['job_title']
            Welding_type = request.POST['Welding_type']
            cert_type = request.POST['cert_type']
            cert_upload =request.FILES['image']
            profile_photo = request.FILES['profile_photo']
            current_company=request.POST['current_company']
            experience=request.POST['experience']
            city = City.objects.get(id=location)
            var = Resume.objects.create(
                user=user,
                first_name=name,
                surname=surname,
                location=city, 
                job_title=job_title,
                cert_type=cert_type,
                cert_upload=cert_upload,
                welding_type=Welding_type,
                experience=experience,
                current_company=current_company,
                profile_photo=profile_photo
                )
            user.has_resume=True
            user.save()
            var.save()
            messages.info(request,'your resume information  has been updated!')
            return redirect('dashboard')
        cities = City.objects.all()
        return render(request, 'resume/update_resume.html',{'cities':cities})
    else:
        messages.warning(request,'Permission Denied')
        return redirect('dashboard')
    
def update_profile(request):
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
            welding_type = request.POST['Welding_type']
            cert_type = request.POST['cert_type']
            current_company=request.POST['current_company']
            experience=int(request.POST['experience'])

            city = City.objects.get(id=location)
            if resume is None:
                resume = Resume(user=request.user)
            
        
            resume.name=name
            resume.surname=surname
            resume.location=city
            resume.job_title=job_title
            resume.welding_type=welding_type
            resume.cert_type=cert_type
            resume.experience=int(experience)
            resume.current_company=current_company
            
            resume.save()
            messages.info(request,'your resume information  has been updated!')
            return redirect('dashboard')
        user_resume = get_object_or_404(Resume, user=request.user)
        city_id = user_resume.location.id if user_resume.location else None
        cities = City.objects.all()
        return render(request, 'resume/update_profile.html', {'city_id': city_id, 'cities': cities})
    else:
        messages.warning(request,'Permission Denied')
        return redirect('dashboard')
    
#view profile/resume
def resume_details(request,pk):
    resume=Resume.objects.get(pk=pk)
    context={'resume':resume}
    return render(request,'resume/resume_details.html',context)