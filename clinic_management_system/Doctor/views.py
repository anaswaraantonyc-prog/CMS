from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['POST'])
def add_consultation(request):
    serializer = ConsultationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Consultation note added successfully"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_consultation(request, consultationId):
    try:
        consultation = Consultation.objects.get(pk=consultationId)
    except:
        return Response({"error": "Not found"}, status=404)

    serializer = ConsultationSerializer(consultation, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Consultation updated"})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_consultation_by_appointment(request, appointmentId):
    data = Consultation.objects.filter(appointment_id=appointmentId)
    serializer = ConsultationSerializer(data, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def create_medicine_prescription(request):
    serializer = MedicinePrescriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Medicine prescription created successfully"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_medicine_prescription(request, prescriptionId):
    obj = MedicinePrescription.objects.get(pk=prescriptionId)
    serializer = MedicinePrescriptionSerializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Medicine prescription updated successfully"})
    return Response(serializer.errors)


@api_view(['GET'])
def get_prescription_by_appointment(request, appointmentId):
    data = MedicinePrescription.objects.filter(appointment_id=appointmentId)
    return Response(MedicinePrescriptionSerializer(data, many=True).data)
@api_view(['POST'])
def create_lab_test(request):
    serializer = LabTestPrescriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Lab test prescription created successfully"}, status=201)
    return Response(serializer.errors)


@api_view(['PUT'])
def update_lab_test(request, prescriptionId):
    obj = LabTestPrescription.objects.get(pk=prescriptionId)
    serializer = LabTestPrescriptionSerializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Lab test prescription updated successfully"})
    return Response(serializer.errors)
