# Generated by Django 4.2.7 on 2024-06-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='Default description'),
        ),
    ]
