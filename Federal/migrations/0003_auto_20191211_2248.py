# Generated by Django 2.1.7 on 2019-12-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0002_executive_related_ministry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='related_files',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
