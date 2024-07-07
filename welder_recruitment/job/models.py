from django.db import models
from users.models import User
from company.models import Company,State,City

from datetime import datetime
import pytz




class Job(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    state=models.ForeignKey(State,on_delete=models.CASCADE,blank=True,null=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,blank=True,null=True)
    salary=models.PositiveIntegerField()
    vacancy=models.PositiveIntegerField()
    exp_requried=models.PositiveIntegerField(null=True)
    description=models.TextField(default='Default description')
    is_available=models.BooleanField(default=True)
    timestamp=models.DateTimeField()
    
    def __str__(self):
        return self.title if self.title else "No Title"
    def save(self, *args, **kwargs):
        # Set the timestamp to the current time in IST if not already set
        if not self.timestamp:
            ist = pytz.timezone('Asia/Kolkata')
            self.timestamp = datetime.now(ist)
        super(Job, self).save(*args, **kwargs)
    
class Applyjobs(models.Model):
    status_choices=(
        ('Accepted','Accepted'),
        ('Declined','Declined'),
        ('Pending','Pending'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    status=models.CharField(max_length=20 ,choices=status_choices)
    remarks=models.CharField(max_length=200,blank=True,null=True)

    def save(self, *args, **kwargs):
        # Set the timestamp to the current time in IST if not already set
        if not self.timestamp:
            ist = pytz.timezone('Asia/Kolkata')
            self.timestamp = datetime.now(ist)
        super(Applyjobs, self).save(*args, **kwargs)