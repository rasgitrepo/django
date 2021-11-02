# Generated by Django 3.2.7 on 2021-11-02 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0008_auto_20211028_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['contact_type'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('contact_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.contacttype')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.people')),
            ],
        ),
    ]
