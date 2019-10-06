from django.contrib import admin
from . models import Medicine, Prescription, Prescription_Medicine



# Register your models here.
admin.site.register([Medicine, Prescription, Prescription_Medicine])