# Generated by Django 3.2.7 on 2021-10-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_alter_linkfamilymember_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='import_key',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
