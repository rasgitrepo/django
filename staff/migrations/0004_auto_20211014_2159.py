# Generated by Django 3.2.7 on 2021-10-14 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_department_linkstaffdepartment_staffrole'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='parent_dept_id',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='linkstaffdepartment',
            old_name='role',
            new_name='staff_role',
        ),
        migrations.RenameField(
            model_name='staffrole',
            old_name='role',
            new_name='staff_role',
        ),
    ]
