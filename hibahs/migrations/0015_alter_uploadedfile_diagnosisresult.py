# Generated by Django 4.2.6 on 2023-11-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibahs', '0014_alter_uploadedfile_diagnosisresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='diagnosisResult',
            field=models.TextField(blank=True, null=True),
        ),
    ]
