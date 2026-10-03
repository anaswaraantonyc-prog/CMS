from django.contrib import admin
from .models import *

admin.site.register(Appointment)
admin.site.register(MedicinePrescription)
admin.site.register(LabTestPrescription)


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['consultation_id', 'appointment', 'diagnosis']