# Generated by Django 5.1.5 on 2025-01-22 12:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('doctorName', models.CharField(max_length=20)),
                ('doctorSpeciality', models.CharField(max_length=20)),
                ('doctorExperience', models.CharField(max_length=20)),
                ('doctorQualification', models.CharField(max_length=20)),
            ],
        ),
    ]
