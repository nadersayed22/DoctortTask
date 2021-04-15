from .models import Patient, Doctor, Clinic
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'gender']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'doctor_email']


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

