# Create your models here.
from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.hashers import make_password

# Create your models here.

class Passwd(models.Model):

    name=models.CharField(max_length=200)   
    link=models.URLField()
    password=models.CharField(max_length=500)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
   
    def __str__(self):
        return self.name