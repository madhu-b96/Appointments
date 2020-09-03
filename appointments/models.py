from django.db import models


class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_age = models.IntegerField()
    
   
    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    Doctor_name =  models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
  

    def __str__(self):
        return self.Doctor_name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    patient_Disease = models.CharField(max_length=200,default="sick")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date_appoint = models.DateField()
    

    def __str__(self):
        return self.date_appoint

