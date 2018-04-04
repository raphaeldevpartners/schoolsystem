import django_filters.rest_framework
from rest_framework.decorators import detail_route, action

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from statsd.defaults.django import statsd

from rest_framework import permissions, generics
from rest_framework.viewsets import ModelViewSet
from studentclasses.serializers import LectureSerializer, RoomSerializer, ScheduleSerializer, StudentSerializer, StudentlectureSerializer, SubjectSerializer, TeacherSerializer
from studentclasses.models import Lecture, Room, Schedule, Student, Studentlecture, Subject, Teacher

class StudentlectureViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = StudentlectureSerializer
    queryset = Studentlecture.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #/studentlectures/{pk}/get_studlect/ gives the lectures of student pk
    @action(detail=True)
    def get_studlect(self, request, *args, **kwargs):
        student_lectures = Studentlecture.objects.all().filter(student_id=self.kwargs['pk'])
        serializer = self.get_serializer(student_lectures, many=True)
        return Response(serializer.data)

    #/studentlectures/{pk}/get_lectstud/ gives the students of lecture pk
    @action(detail=True)
    def get_lectstud(self, request, *args, **kwargs):
        lecture_students = Studentlecture.objects.all().filter(lecture_id=self.kwargs['pk'])
        serializer = self.get_serializer(lecture_students, many=True)
        return Response(serializer.data)


class LectureViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = ()

    #/lectures/{pk}/get_teachlect/ gives the lectures of teacher pk
    @action(detail=True)
    def get_teachlect(self, request, *args, **kwargs):
        teacher_lectures = Lecture.objects.all().filter(teacher_id=self.kwargs['pk'])
        serializer = self.get_serializer(teacher_lectures, many=True)
        return Response(serializer.data)

class RoomViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class ScheduleViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

class StudentViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SubjectViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class TeacherViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

# http://127.0.0.1:8000/custom/get/ TEST for customized url patterns in urls.py
class CustomGet(APIView):
  """
  A custom endpoint for GET request.
  """
  def get(self, request, format=None):
    """
    Return a hardcoded response.
    """
    return Response({"success": True, "content": "Hello Dragons!"})
