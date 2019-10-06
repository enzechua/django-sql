from django.db import models



# Create your models here.
class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    prescription_timestamp = models.DateField()
    medicine = models.ManyToManyField(Medicine, through='prescription_medicine')


class Prescription_Medicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    medicine_dosage = models.IntegerField()

    class Meta:
        unique_together = ['prescription', 'medicine']








