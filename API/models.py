from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

class Doctor(models.Model):
    doctorId = models.UUIDField(default=uuid.uuid4, editable = False, unique = True, primary_key=True)
    doctorName = models.CharField(max_length=20, blank=False)
    doctorSpeciality = models.CharField(max_length=20, blank=False)
    doctorExperience = models.CharField(max_length=20,blank=False)
    doctorQualification = models.CharField(max_length=20,blank=False)
    doctorImage = models.ImageField(default="default.png", blank=True)
    
    def __str__(self):
        return "Dr. " + self.doctorName+ " " + self.doctorSpeciality
    