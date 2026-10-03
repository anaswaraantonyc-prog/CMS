from django.db import models

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    consultation_status = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    notes = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class MedicinePrescription(models.Model):
    medicine_prescription_id = models.AutoField(primary_key=True)
    medicine_id = models.IntegerField()
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class LabTestPrescription(models.Model):
    lab_test_prescription_id = models.AutoField(primary_key=True)
    lab_test_id = models.IntegerField()
    lab_test_value = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
# Create your models here.
