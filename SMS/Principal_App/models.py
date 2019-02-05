from django.db import models
from django.utils import timezone
import uuid
from Student_App.models import Student
from Teacher_App.models import Teacher

class Timetable(models.Model):
    Tmid = models.IntegerField()
    Tid = models.ForeignKey(Teacher,models.SET_NULL,blank=True,null=True)
    room_no = models.IntegerField()
    time = models.TimeField()
    day = models.CharField(max_length=20)

class Meta:
    db_table = "TimeTable"


class Principal(models.Model):
    Pid = models.IntegerField()
    PTid = models.ForeignKey(Teacher, models.SET_NULL, blank=True, null=True)
    PSId = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)
    PFname = models.CharField(max_length=20)
    PLname = models.CharField(max_length=20)
    Pemail = models.EmailField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Pgender = models.CharField(max_length=1, choices=GENDER_CHOICES)