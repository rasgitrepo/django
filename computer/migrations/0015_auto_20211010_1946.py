# Generated by Django 3.2.7 on 2021-10-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0014_auto_20211010_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='computer',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='staff',
        ),
    ]