# Generated by Django 5.0.7 on 2024-07-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_rename_admin_hod'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.FileField(blank=True, default='attendance/static/students/default.jpeg', null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'Hod')]),
        ),
    ]