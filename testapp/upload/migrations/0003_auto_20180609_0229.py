# Generated by Django 2.0.5 on 2018-06-09 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='Number',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='Status',
        ),
    ]
