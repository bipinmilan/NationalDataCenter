# Generated by Django 2.1.7 on 2019-12-12 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0004_auto_20191212_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executive',
            name='author',
        ),
    ]