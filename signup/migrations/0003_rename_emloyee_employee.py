# Generated by Django 4.1.1 on 2022-09-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_emloyee_alter_student_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emloyee',
            new_name='Employee',
        ),
    ]