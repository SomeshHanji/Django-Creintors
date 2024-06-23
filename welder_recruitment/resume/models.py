from django.db import models
from users.models import User
from welder_recruitment import settings
from company.models import City

class Resume(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    surname=models.CharField(max_length=100,null=True,blank=True)
    location=models.ForeignKey(City,on_delete=models.CASCADE, null=True,blank=True)
    job_title=models.CharField(max_length=100,null=True,blank=True)
    cert_type=models.CharField(max_length=200,blank=True)
    welding_type=models.CharField(max_length=200,blank=True)
    cert_upload=models.ImageField(upload_to="",blank=True)
    current_company=models.CharField(max_length=100,null=True,blank=True)
    experience=models.PositiveIntegerField(null=True,blank=True)
    profile_photo=models.ImageField(upload_to="",blank=True)

    def __str__(self):
        return f'{self.first_name}{self.surname}'
        