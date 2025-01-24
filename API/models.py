from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    profileAge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)], blank = False, default = 0)
    profileGender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default = "M")


def __str__(self):
    return str(self.user)

class Doctor(models.Model):
    doctorId = models.UUIDField(default=uuid.uuid4, editable = False, unique = True, primary_key=True)
    doctorName = models.CharField(max_length=20, blank=False)
    doctorSpeciality = models.CharField(max_length=20, blank=False)
    doctorExperience = models.CharField(max_length=20,blank=False)
    doctorQualification = models.CharField(max_length=20,blank=False)
    doctorImage = models.ImageField(default="default.jpg", blank=True)


def __str__(self):
    return "Dr. " + self.doctorName+ " " + self.doctorSpeciality