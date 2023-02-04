from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Amenity(models.Model):
    description = models.CharField(max_length=50)


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

    # add generic relations to our comments to our Events to implement polymorphic relations
    # https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#id1
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['creation_time']

    def __str__(self):
        return self.content


class Location(models.Model):
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Event(models.Model):
    creator = models.CharField(max_length=50)  # this should be something else
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    meetup_time = models.DateTimeField()

    # We add a GenericRelation field to our Event base class as GenericForeignKeys don't
    # automatically generate reverse relations (to Comment in this case)
    comments = GenericRelation(Comment)

    class Meta:
        ordering = ['creation_time']


class StudyGroup(Event):
    amenities = models.ManyToManyField(Amenity)
