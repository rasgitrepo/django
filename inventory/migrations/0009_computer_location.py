# Generated by Django 3.2.7 on 2021-10-29 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('inventory', '0008_computer_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.location'),
        ),
    ]