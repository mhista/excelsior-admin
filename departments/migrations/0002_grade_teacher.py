# Generated by Django 3.2.5 on 2023-06-12 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.teacher'),
        ),
    ]