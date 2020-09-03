from rest_framework import routers
from appointments.viewsets import PatientViewset,DoctorViewset,ApoointViewset

routers = routers.DefaultRouter()
routers.register('Patients',PatientViewset)
routers.register('Doctors',DoctorViewset)
routers.register('appointments',ApoointViewset)