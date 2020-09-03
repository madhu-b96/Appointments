from rest_framework import viewsets
from .models import Patient,Doctor,Appointment
from .serializers import PatientSerializer,DoctorSerializer,AppointSerializer

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ApoointViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointSerializer        