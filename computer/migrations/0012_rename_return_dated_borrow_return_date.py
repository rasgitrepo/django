# Generated by Django 3.2.7 on 2021-10-10 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0011_auto_20211010_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='return_dated',
            new_name='return_date',
        ),
    ]
