# Generated by Django 3.2.7 on 2021-10-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20211010_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'ordering': ('brand', 'model')},
        ),
        migrations.AlterField(
            model_name='borrow',
            name='issued_by',
            field=models.CharField(blank=True, choices=[('Diaw', 'Diaw'), ('Jonathan', 'Jonathan'), ('Jo', 'Jo'), ('Em', 'Em Kanapot')], max_length=100, null=True),
        ),
    ]
