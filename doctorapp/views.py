from django.shortcuts import render
from .serializer import DoctorSerializer, PatientSerializer, ClinicSerializer
from .models import Clinic, Doctor, Patient
from rest_framework import generics


# Create your views here.
class ServListCreateAPIView(generics.ListCreateAPIView):
    """
    List Create API for clinic table
    """
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class DoctorListCreateAPIView(generics.ListCreateAPIView):
    """
    List Create API for Doctor table
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientListCreateAPIView(generics.ListCreateAPIView):
    """
    List Create API for patient table
    """
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ServRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Update Destroy API for Clinic table
    """
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Update Destroy API for Doctor
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Update Destroy API for Patient table
    """
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
