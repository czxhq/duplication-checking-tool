# Generated by Django 3.2.8 on 2024-07-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20240729_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='duser',
            name='is_sec',
            field=models.BooleanField(default=False),
        ),
    ]
