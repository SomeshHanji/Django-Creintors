# Generated by Django 4.2.7 on 2024-06-17 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_resume_welding_type_alter_resume_cert_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='current_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
