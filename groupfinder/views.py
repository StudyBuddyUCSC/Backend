from rest_framework.fields import CurrentUserDefault
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from groupfinder.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class AmenityList(generics.ListAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated]


class AmenityAdd(generics.CreateAPIView):
    """Lets an admin add an amenity."""
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAdminUser]


class StudyGroupList(generics.ListCreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class StudyGroupUpdate(generics.RetrieveUpdateDestroyAPIView):
    # maybe this should be in the serializer?
    queryset = StudyGroup.objects.filter(creator=CurrentUserDefault())
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

