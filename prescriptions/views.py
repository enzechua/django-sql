from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, renderers # new
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import PrescriptionMedicineSerializers, PrescriptionSerializers
from .models import Prescription_Medicine, Prescription
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#
#


class PrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PrescriptionSerializers
    queryset = Prescription.objects.all()


class MedicineDetail(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializers












