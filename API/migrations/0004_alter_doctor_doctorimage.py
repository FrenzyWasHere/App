# Generated by Django 5.1.5 on 2025-01-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_doctor_doctorimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctorImage',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
