from rest_framework import serializers
from groupfinder.models import *


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['description']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['creator', 'content']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['longitude', 'latitude', 'address']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['creator', 'location', 'creation_time', 'meetup_time', 'comments']


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ['creator', 'location', 'creation_time', 'meetup_time', 'comments', 'amenities']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # We will serialize all fields; leave fields var blank
