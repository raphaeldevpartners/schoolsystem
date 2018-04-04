from rest_framework import serializers
from studentclasses.models import Lecture, Room, Schedule, Student, Studentlecture, Subject, Teacher

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'id', 'student_code', 'first_name', 'last_name')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'id', 'teacher_code', 'first_name', 'last_name')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'id', 'subject_name')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'id', 'room_name')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('url', 'id', 'room', 'time_start', 'time_end')

class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('url', 'id', 'lecture_name', 'subject', 'teacher', 'schedule')

class StudentlectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studentlecture
        fields = ('url', 'id', 'lecture', 'student')
