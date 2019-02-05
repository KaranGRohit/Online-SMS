from django.db import models
from django.utils import timezone
import uuid
from Student_App.models import Student


class Teacher(models.Model):
    TID = models.UUIDField( primary_key=True , default = uuid.uuid4)
    #TStuds = models.OneToManyField(Student,symmetrical=False)
    TSId = models.ForeignKey(Student,models.SET_NULL,blank=True,null=True)
    TFName = models.CharField(max_length=30)
    TLname = models.CharField(max_length=30,blank=True)
    TCity = models.CharField(max_length=20,blank=True)
    TEmail = models.EmailField(max_length=30,blank=True)
    TClass = models.IntegerField(blank=True)
    TSubject = models.CharField(max_length=20)

class Meta:
    db_table = "Teacher"


class Result(models.Model):
    Roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
    Rid = models.IntegerField()
    grade = models.CharField(max_length=4)
    sub1 = models.CharField(max_length=20)
    sub2 = models.CharField(max_length=20)
    sub3 = models.CharField(max_length=20)
    marks1 = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()

class Meta:
    db_table = "Result"

#class Attendance(models.Model):
 #   Roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
  #  Aid = models.IntegerField()
   # attendance = models.IntegerField()


class Assignments(models.Model):
    Aid = models.IntegerField()
    Roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    assingment = models.CharField(max_length=30)
    deadline = models.DateField()
    submit_status = models.BooleanField()

class Meta:
    db_table = "Assignments"



