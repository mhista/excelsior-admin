# Generated by Django 3.2.5 on 2023-06-13 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.data'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='marital_status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]