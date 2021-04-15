from django.contrib import admin
from .models import Patient, Doctor, Clinic

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Clinic)
