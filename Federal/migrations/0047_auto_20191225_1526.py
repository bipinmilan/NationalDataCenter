# Generated by Django 2.1.7 on 2019-12-25 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0046_auto_20191225_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executive',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='judiciary',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='legislative',
            name='deleted_at',
        ),
    ]