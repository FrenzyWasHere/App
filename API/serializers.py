from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Doctor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name']
        
class DoctorSerializer(serializers.Model):
    class Meta:
        model = Doctor
        fields = '__all__'