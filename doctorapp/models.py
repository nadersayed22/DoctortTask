from django.db import models

# Create your models here.
gender = (
    ('male', 'male'),
    ('female', 'female')
)


class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=25, choices=gender)


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    doctor_email = models.EmailField(max_length=255, unique=True)


class Clinic(models.Model):
    clinic_name = models.CharField(max_length=255)
    price = models.IntegerField()
    date_serve = models.DateField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    patient_serv = models.ForeignKey('patient', on_delete=models.CASCADE)
    doctor_serv = models.ForeignKey('Doctor', on_delete=models.CASCADE)
