# Generated by Django 3.2.5 on 2023-06-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
    ]