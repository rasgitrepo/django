# Generated by Django 3.2.7 on 2021-10-29 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idcard', '0002_idcard_barcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idstatus',
            options={'ordering': ['id_status'], 'verbose_name_plural': 'Job Types'},
        ),
    ]
