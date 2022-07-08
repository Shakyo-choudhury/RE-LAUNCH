from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.

#contact
class Contact(models.Model):
    name= models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    username=models.CharField(max_length=1000)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name  
#message
class Msg(models.Model):
    name1=models.CharField(max_length=200)
    msg=models.TextField()
    date1=models.DateField()
    def __str__(self):
        return self.name1    
#search(not working)
class Search(models.Model):
    search=models.TextField()
    def __str__(self):
        return self.search
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    Location=models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.name


class Candidates(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    )

    name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    gender= models.CharField(max_length=200,null=True,choices=category)
    mobile= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    resume=models.FileField(null=True)
    company=models.ManyToManyField(Company,blank=True)

    def __str__(self):
        return self.name



