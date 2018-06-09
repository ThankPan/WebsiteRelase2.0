# Generated by Django 2.0.5 on 2018-06-09 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Upload_time', models.DateTimeField()),
                ('File', models.FileField(upload_to='')),
                ('Homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Homework')),
                ('Student', models.ForeignKey(default='44436', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
