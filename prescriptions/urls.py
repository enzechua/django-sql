from django.contrib import admin
from django.urls import path, include
from .views import PrescriptionViewSet, MedicineDetail



urlpatterns = [
    # path('medical-details/', PrescriptionViewSet.as_view({'get': 'list'})),
    path('medical-details/', MedicineDetail.as_view()),
]


