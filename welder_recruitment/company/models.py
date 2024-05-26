from django.db import models
from users.models import User
from welder_recruitment import settings

class Company(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    est_date=models.PositiveIntegerField(null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) :
        return self.name
