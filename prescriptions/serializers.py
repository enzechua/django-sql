from rest_framework import serializers
from .models import Medicine, Prescription, Prescription_Medicine


class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        # fields = '__all__'
        fields = ['name', 'description']


class PrescriptionMedicineSerializers(serializers.ModelSerializer):
    medicine = MedicineSerializers()
    # medicine_id = serializers.ReadOnlyField(source='medicine.name')
    # medicine_description = serializers.SerializerMethodField(source='medicine.description')

    class Meta:
        model = Prescription_Medicine
        fields = ['medicine', 'medicine_dosage']

    # def create(self, validated_data):
    #     print(validated_data)
    # def create(self, validated_data):
    #     prescription = validated_data.pop('prescription')
    #     medicine_list = prescription.pop('medicine')
    #
    #     prescription_obj = Prescription.objects.create(**prescription)
    #     validated_data['prescription'] = prescription_obj
    #
    #     for medicine in medicine_list:
    #         # print(medicine)
    #         # check if medicine has been created before.
    #         medicine = Medicine.objects.create(**medicine)
    #
    #         prescription_medicine = Prescription_Medicine.objects.create(**validated_data, medicine=medicine)
    #
    #     return prescription_medicine


class PrescriptionSerializers(serializers.ModelSerializer):

    medicine_list = PrescriptionMedicineSerializers(many=True, source='prescription_medicine_set')

    class Meta:
        model = Prescription
        fields = ['id', 'medicine_list', 'prescription_timestamp']
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        medicine_list = validated_data.pop('prescription_medicine_set')
        print(validated_data)
        prescription_obj = Prescription.objects.create(**validated_data)
        print(medicine_list)
        for medicineAndDosage in medicine_list:
            medicine = medicineAndDosage.pop('medicine')
            medicine_dosage = medicineAndDosage['medicine_dosage']

            medicine_obj = Medicine.objects.create(**medicine)
            Prescription_Medicine.objects.create(
                prescription=prescription_obj,
                medicine=medicine_obj,
                medicine_dosage=medicine_dosage)

        return prescription_obj
