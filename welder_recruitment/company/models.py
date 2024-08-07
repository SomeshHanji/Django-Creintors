from django.db import models
from users.models import User
from welder_recruitment import settings
class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name if self.name else "Unnamed State"

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name if self.name else "Unnamed State"
    
class Company(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    est_date=models.PositiveIntegerField(null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    gst_number = models.CharField(max_length=15, unique=True,blank=True,null=True)
    desc=models.TextField(default='Default description')

    def __str__(self) :
        return self.name if self.name else "Unnamed Company"
