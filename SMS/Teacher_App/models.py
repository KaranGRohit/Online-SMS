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
