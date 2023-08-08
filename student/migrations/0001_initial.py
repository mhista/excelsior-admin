# Generated by Django 3.2.5 on 2023-06-07 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('reg_number', models.CharField(max_length=5)),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.data')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.data')),
            ],
        ),
    ]
