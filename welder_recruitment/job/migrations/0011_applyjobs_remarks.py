# Generated by Django 4.2.7 on 2024-06-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_remove_job_location_remove_job_requirements_job_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjobs',
            name='remarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
