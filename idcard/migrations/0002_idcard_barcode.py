# Generated by Django 3.2.7 on 2021-10-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idcard',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
