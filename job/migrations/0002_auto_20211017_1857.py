# Generated by Django 3.2.7 on 2021-10-17 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobaction',
            options={'verbose_name_plural': 'Job Action'},
        ),
        migrations.AlterModelOptions(
            name='jobstatus',
            options={'verbose_name_plural': 'Job Status'},
        ),
        migrations.AlterModelOptions(
            name='jobtype',
            options={'verbose_name_plural': 'Job Type'},
        ),
    ]
