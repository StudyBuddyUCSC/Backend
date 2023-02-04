from rest_framework import serializers
from models import *


class AmenitySerializer:
    class Meta:
        model = Amenity
        fields = ['description']


class CommentSerializer:
    class Meta:
        model = Comment
        fields = ['creator', 'content']


class LocationSerializer:
    class Meta:
        model = Location
        fields = ['longitude', 'latitude', 'address']


class EventSerializer:
    class Meta:
        model = Event
        fields = ['creator', 'location', 'creation_time', 'meetup_time', 'comments']


class StudyGroup:
    class Meta:
        model = Event
        fields = ['amenities']
