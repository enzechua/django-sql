# Generated by Django 2.2.6 on 2019-10-05 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription_timestamp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription_Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_dosage', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescriptions.Medicine')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescriptions.Prescription')),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='medicines',
            field=models.ManyToManyField(through='prescriptions.Prescription_Medicine', to='prescriptions.Medicine'),
        ),
    ]
