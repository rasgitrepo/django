# Generated by Django 3.2.7 on 2021-10-28 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0005_alter_linkstaffdepartment_active'),
        ('people', '0008_auto_20211028_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_status', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['id_status'],
            },
        ),
        migrations.CreateModel(
            name='IDType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['id_type'],
            },
        ),
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(blank=True, null=True)),
                ('card_number', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='idcard.idstatus')),
                ('id_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='idcard.idtype')),
                ('issued_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issued_by', to='staff.staff')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_holder', to='people.people')),
            ],
        ),
    ]
