# Generated by Django 3.2.5 on 2023-06-12 21:13

from django.db import migrations, models
import django.db.models.deletion
import school.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20230607_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='photo',
            field=models.ImageField(null=True, upload_to=school.file_upload.item_files_directory),
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
