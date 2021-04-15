from django.urls import path
from .views import ServListCreateAPIView, DoctorListCreateAPIView, PatientListCreateAPIView
from .views import ServRetrieveUpdateDestroyAPIView, DoctorRetrieveUpdateDestroyAPIView, PatientRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', ServListCreateAPIView.as_view(), name="reservations"),
    path('<int:pk>/', ServRetrieveUpdateDestroyAPIView.as_view(), name='get_serves'),

    path('doctors/', DoctorListCreateAPIView.as_view(), name="doctors"),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name="get_doctors"),

     path('patients/', PatientListCreateAPIView.as_view(), name="patients"),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name="get_patient"),

]
