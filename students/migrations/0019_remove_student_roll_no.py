# Generated by Django 5.0.7 on 2024-07-29 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_student_roll_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
    ]