# Generated by Django 3.2.7 on 2021-10-30 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_dropoffpickup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linkstudentcourse',
            options={'ordering': ['student'], 'verbose_name_plural': "Add/Remove Student's course"},
        ),
    ]