from django.db import models

# Create your models here.
class Trial(models.Model):
    fname=models.CharField(max_length=100) 
    lname=models.CharField(max_length=100) 
    sdate=models.DateField()
    edate=models.DateField()
    course=models.CharField(max_length=50)
    