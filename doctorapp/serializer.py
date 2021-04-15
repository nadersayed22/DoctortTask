from .models import Patient, Doctor, Clinic
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'gender']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'doctor_name', 'doctor_email']


class Clinic(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'
