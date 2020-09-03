from rest_framework import serializers
from .models import Patient,Doctor,Appointment

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class AppointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
                