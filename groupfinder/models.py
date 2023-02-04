from django.db import models
from django.contrib.auth.models import User


class Amenity(models.Model):
    description = models.CharField(max_length=50)


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']


class Location(models.Model):
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Event(models.Model):
    creator = models.CharField(max_length=50)  # this should be something else
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    meetup_time = models.DateTimeField()
    comments = models.ManyToManyField(Comment)


class StudyGroup(Event):
    amenities = models.ManyToManyField(Amenity)


