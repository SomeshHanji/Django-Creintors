from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Company
from users.models import User


def update_company(request):
    if request.user.is_recruiter:
        try:
            company = Company.objects.get(user=request.user)
            # Check if the company instance is "empty"
            if not company.name and not company.est_date and not company.state and not company.city:
                company = None
        except Company.DoesNotExist:
            company = None
        if request.method == 'POST':
            user = User.objects.get(id=request.user.id)
            userid=user.id
            name = request.POST['name']
            est_date = request.POST['est_date']
            state = request.POST['state']
            city = request.POST['city']
            var = Company.objects.create(user=user, name=name, est_date=est_date, state=state, city=city)
            user.has_company=True
            user.save()
            var.save()
            messages.info(request,'your company information  has been updated!')
            return redirect('dashboard')
        return render(request, 'company/update_company.html')
    else:
        messages.warning(request,'Permission Denied')
        return redirect('dashboard')
    


    
#view company details
def company_details(request,pk):
    company=Company.objects.get(pk=pk)
    context={'company':company}
    return render(request,'company/company_details.html',context)
#create jobs   
def update_jobs(request):
    return render(request,'company/update_job.html')


# update company test 1
# def update_company(request):
#     try:
#         company = Company.objects.get(user=request.user)
#     except Company.DoesNotExist:
#         return render(request,'company/update_company.html')
#     if request.method == 'POST':
#         form = UpdateCompanyForm(request.POST,instance=company)
#         if form.is_valid():
#             var=form.save(commit=False)
#             user=User.objects.get(id=request.user.id)
#             user.has_company =True 
#             var.save()
#             user.save()
#             messages.info(request,'your company is now active.')
#             return redirect('dashboard')
#         else:
#             messages.warning(request,'Something Went Wrong')
#     else:
#         form=UpdateCompanyForm(instance=company)
#         context={'form':form}
#         return render(request,'company/update_company.html')

#update Company profile test 2
# def update_company(request):
#     try:
#         company = Company.objects.get(user=request.user)
#     except Company.DoesNotExist:
#         return render(request,'company/update_company.html')
#     if request.method == 'POST':
#         name = request.POST['name']
#         est_date = request.POST['est_date']
#         state = request.POST['state']
#         city = request.POST['city']
#         user=request.user
#         user.has_company=True
#         company = Company.objects.create(user=user,name=name, est_date=est_date, state=state, city=city)
#         user.save()
#         messages.info(request,'your company is now active.')
#         return redirect('dashboard')
#     else:
        
#         return render(request,'company/update_company.html')

    