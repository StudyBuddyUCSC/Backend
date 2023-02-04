from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.fields import CurrentUserDefault
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from groupfinder.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]


class AmenityList(generics.ListAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    # permission_classes = [IsAuthenticated]


class AmenityAdd(generics.CreateAPIView):
    """Lets an admin add an amenity."""
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    # permission_classes = [IsAdminUser]


class StudyGroupList(generics.ListCreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    # permission_classes = [IsAuthenticated]


class StudyGroupUpdate(generics.RetrieveUpdateDestroyAPIView):
    # maybe this should be in the serializer?
    queryset = StudyGroup.objects.filter(creator=CurrentUserDefault())
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticated]


class LocationsGet(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = [IsAuthenticated]


class LocationUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = [IsAdminUser]


class LocationAdd(generics.CreateAPIView):
    serializer_class = LocationSerializer


class GetStudyGroupComments(APIView):
    # permission_classes = [IsAuthenticated]

    def get_studygroup_comments(self, pk):
        try:
            study_group = StudyGroup.objects.get(pk=pk)
            return study_group.comments.all()
        except StudyGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comments = [comment.content for comment in self.get_studygroup_comments(pk)]
        return Response(comments)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
