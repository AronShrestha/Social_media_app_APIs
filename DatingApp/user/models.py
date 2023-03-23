from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class User(AbstractUser):
    gender_choices = (
    ("M","Male"),
    ("F","Female"),
    ("O","Other")
)
    dob = models.DateTimeField(default=None,null=True,blank=True)
    country  = models.CharField(max_length = 200,default=None,null=True,blank=True)
    city = models.CharField(max_length = 220,default=None,null=True,blank=True)
    gender = models.CharField(max_length = 40,default=None,null=True,blank=True,choices=gender_choices)
    interest = models.CharField(max_length = 670,default=None,null=True,blank=True)
    

    def __str__(self) -> str:
        return str(self.username)





#  "username": "Arjjon",
#  "email" : "arojjn@gamail.com",
#  "password" : "a",

#  "Country" :"Nepal",
#  "dob" : "2010-04-20T20:08:21.634121",
#  "city":"Kathmandu",
#  "gender":"M",
#  "interest" :"Playing",
#  "country" :"USA"