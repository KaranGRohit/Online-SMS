from django.db import models
from django.utils import timezone
import uuid

class Student(models.Model):
    SID = models.UUIDField( primary_key=True , default = uuid.uuid4)
    SFName = models.CharField(max_length=20)
    SLname = models.CharField(max_length=30,null=True)
    SAddress = models.CharField(max_length=80,null=True)
    SEmail = models.EmailField(max_length=30,null=True)
    SClass = models.IntegerField(null=True)

class Meta:
    db_table = "Student"