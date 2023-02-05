from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=30) #What is 
    location_type = models.CharField(max_length=30) #Is it a library or a classroom or a cafe?
    campus_location = models.CharField(max_length=30) #Where is it on campus?
    allhouraccess = models.BooleanField(default=True) #Is it 24 hour access?
    genderneutralbathroom = models.BooleanField(default=True) #We define this as if there is an inclusive bathroom within 1300 ft


# Create your models here.
