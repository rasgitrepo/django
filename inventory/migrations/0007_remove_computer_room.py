# Generated by Django 3.2.7 on 2021-10-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20211029_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='room',
        ),
    ]
