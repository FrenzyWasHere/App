from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    profileAge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)], blank = False, default = 0)
    profileGender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default = "M", blank=False)
    profileImage = models.ImageField(null=True, upload_to="uploads/")

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



class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    appointmentId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    userProfile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointmentDateTime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"Appointment {self.appointmentId} with {self.doctor} on {self.appointmentDateTime}"