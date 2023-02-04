from django.db import models
from django.contrib.auth.models import User


class Amentity():
    description = models.CharField()


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']


class Locations(models.Model):
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Events(models.Model):
    creator = models.CharField(max_length=50)  # this should be something else
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    creationTime = models.DateTimeField(auto_now_add=True)
    meetup_time = models.DateTimeField()
    comments = models.ManyToManyField(Comment)


class StudyGroup(Events):
    amentities = models.ManyToManyField(Amentity)


