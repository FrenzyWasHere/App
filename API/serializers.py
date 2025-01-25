from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Doctor, Appointment
from django.contrib.auth.hashers import check_password

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profileID', 'profileAge', 'profileGender', 'profileImage']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    current_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'first_name', 'last_name', 'profile', 'current_password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}  #Crucial change

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        current_password = validated_data.pop('current_password', None)

        # Check if the current password is correct (Crucial check)
        if current_password:
            if not check_password(current_password, instance.password):
                raise serializers.ValidationError({'current_password': 'Incorrect password.'})

        # Important:  Don't update password unless it was sent
        # and don't allow updating password without current password
        if 'password' in validated_data and current_password is None:
           raise serializers.ValidationError({'password': 'Must provide current password to change.'})

        # Update user fields
        for field, value in validated_data.items():
            if field in ['username', 'email', 'first_name', 'last_name'] and value is not None:
                setattr(instance, field, value)

        # Update password if provided and current password was checked
        if 'password' in validated_data and current_password:
           instance.set_password(validated_data['password'])


        instance.save()

        # Update profile fields
        if profile_data:
            try:
                profile = instance.profile
                for attr, value in profile_data.items():
                    setattr(profile, attr, value)
                profile.save()
            except AttributeError:
                raise serializers.ValidationError({'profile': 'Profile not found'})  # Handle missing profile

        return instance


# ... (other serializers)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctorId', 'doctorName', 'doctorSpeciality', 'doctorExperience', 'doctorQualification', 'doctorImage']
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'