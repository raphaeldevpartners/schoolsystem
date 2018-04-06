from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student_code}'

class Teacher(models.Model):
     teacher_code = models.CharField(max_length=20)
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)

     def __str__(self):
         return f'{self.teacher_code}'

class Subject(models.Model):
     subject_name = models.CharField(max_length=20)

     def __str__(self):
         return f'{self.subject_name}'

class Room(models.Model):
     room_name = models.CharField(max_length=20)

     def __str__(self):
         return f'{self.room_name}'

class Schedule(models.Model):
     room = models.ForeignKey(Room, on_delete=models.CASCADE)
     time_start = models.TimeField(max_length=20)
     time_end = models.TimeField(max_length=20)

     def __str__(self):
         return f'{self.time_start} {self.time_end}'

class Lecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=20, default='Lecture for Dragons')

    def __str__(self):
        return f'{self.lecture_name}'

class Studentlecture(models.Model):
    student = models.ForeignKey(Student, default='', on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, default='', on_delete=models.CASCADE)
    studentlecture_name = models.CharField(max_length=20, default='ComputerScience Lectures')

    def __str__(self):
        return f'{self.studentlecture_name}'
