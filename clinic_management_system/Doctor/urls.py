from django.urls import path
from . import views

urlpatterns = [
    path('api/consultations', views.add_consultation),
    path('api/consultations/<int:consultationId>', views.update_consultation),
    path('api/consultations/appointment/<int:appointmentId>', views.get_consultation_by_appointment),

    path('api/prescriptions/medicine', views.create_medicine_prescription),
    path('api/prescriptions/medicine/<int:prescriptionId>', views.update_medicine_prescription),
    path('api/prescriptions/medicine/appointment/<int:appointmentId>', views.get_prescription_by_appointment),

    path('api/prescriptions/labtest', views.create_lab_test),
    path('api/prescriptions/labtest/<int:prescriptionId>', views.update_lab_test),
]