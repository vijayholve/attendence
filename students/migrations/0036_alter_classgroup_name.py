# Generated by Django 5.0.7 on 2024-08-04 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0035_alter_classgroup_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classgroup',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.classes'),
        ),
    ]