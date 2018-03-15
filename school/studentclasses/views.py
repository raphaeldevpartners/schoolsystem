from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from studentclasses.serializers import LectureSerializer, RoomSerializer, ScheduleSerializer, StudentSerializer, StudentlectureSerializer, SubjectSerializer, TeacherSerializer
from studentclasses.models import Lecture, Room, Schedule, Student, Studentlecture, Subject, Teacher

class LectureViewSet(ModelViewSet):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()

class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentlectureViewSet(ModelViewSet):
    serializer_class = StudentlectureSerializer
    queryset = Studentlecture.objects.all()

class SubjectViewSet(ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
