from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Company,State,City
from users.models import User

import re
from django.core.exceptions import ValidationError

def validate_gst_number(gst_number):
    """
    Validate Indian GST number format.
    GST Number Format: 15 characters, alphanumeric.
    First two characters are numbers (State Code).
    The next 10 characters are PAN number.
    The 13th character is a letter.
    The 14th character is a number or letter 'Z'.
    The 15th character is a digit (check digit).
    """
    gst_regex = re.compile('\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}')
    if not gst_regex.match(gst_number):
        raise ValidationError(f'{gst_number} is not a valid GST number')



def update_company(request):
    if request.user.is_recruiter:
        try:
            company = Company.objects.get(user=request.user)
            if not company.name and not company.est_date and not company.state and not company.city:
                company = None
        except Company.DoesNotExist:
            company = None

        if request.method == 'POST':
            user = request.user
            name = request.POST['name']
            gst_number = request.POST['gst_number']
            est_date = request.POST['est_date']
            state_id = request.POST['state']
            city_id = request.POST['city']

            try:
                validate_gst_number(gst_number)
            except ValidationError as e:
                return render(request, 'company/update_company.html', {'company': company, 'states': states, 'cities': cities, 'error': str(e)})

            state = State.objects.get(id=state_id)
            city = City.objects.get(id=city_id)

            if company:
                company.name = name
                company.est_date = est_date
                company.state = state
                company.city = city
                company.gst_number = gst_number
                company.save()
            else:
                company = Company.objects.create(user=user, name=name, est_date=est_date, state=state, city=city, gst_number=gst_number)

            user.has_company = True
            user.save()

            messages.info(request, 'Your company information has been updated!')
            return redirect('dashboard')

        states = State.objects.all()
        cities = City.objects.filter(state=company.state) if company else City.objects.none()

        return render(request, 'company/update_company.html', {'company': company, 'states': states, 'cities': cities})
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')


# def update_company(request):
#     if request.user.is_recruiter:
#         try:
#             company = Company.objects.get(user=request.user)
#             # Check if the company instance is "empty"
#             if not company.name and not company.est_date and not company.state and not company.city:
#                 company = None
#         except Company.DoesNotExist:
#             company = None
#         if request.method == 'POST':
#             user = User.objects.get(id=request.user.id)
#             userid=user.id
#             name = request.POST['name']
#             est_date = request.POST['est_date']
#             state = request.POST['state']
#             city = request.POST['city']
#             var = Company.objects.create(user=user, name=name, est_date=est_date, state=state, city=city)
#             user.has_company=True
#             user.save()
#             var.save()
#             messages.info(request,'your company information  has been updated!')
#             return redirect('dashboard')
#         states = State.objects.all()
#         return render(request, 'company/update_company.html',{'states':states})
#     else:
#         messages.warning(request,'Permission Denied')
#         return redirect('dashboard')
    


    
#view company details
def company_details(request,pk):
    company=Company.objects.get(pk=pk)
    context={'company':company}
    return render(request,'company/company_details.html',context)
#create jobs   
def update_jobs(request):
    return render(request,'company/update_job.html')


def load_cities(request):
    state_id = request.GET.get('state_id')
    print("State ID:", state_id)  # Debug statement
    if state_id:
        cities = City.objects.filter(state_id=state_id).all()
        city_list = list(cities.values('id', 'name'))
        print("City List:", city_list)  # Debug statement
        return JsonResponse(city_list, safe=False)
    return JsonResponse([], safe=False)



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

    