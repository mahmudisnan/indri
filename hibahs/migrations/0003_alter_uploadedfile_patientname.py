# Generated by Django 5.0.dev20230825192722 on 2023-09-01 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibahs', '0002_uploadedfile_patientname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='patientName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hibahs.patientdata'),
        ),
    ]
