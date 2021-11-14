# Generated by Django 3.2.7 on 2021-11-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20211106_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='type',
            field=models.CharField(blank=True, choices=[('All-in-one', 'All-in-one'), ('Desktop', 'Desktop'), ('Document Camera', 'Document Camera'), ('Laptop', 'Laptop'), ('Network', 'Network'), ('Printer', 'Printer'), ('Projector', 'Projector'), ('Server', 'Server'), ('Tablet', 'Tablet'), ('TV/SmartTV', 'TV/SmartTV')], max_length=100, null=True),
        ),
    ]