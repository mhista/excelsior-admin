# Generated by Django 3.2.5 on 2023-06-20 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_student_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='guardian',
        ),
        migrations.AddField(
            model_name='guardian',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.guardian'),
        ),
    ]