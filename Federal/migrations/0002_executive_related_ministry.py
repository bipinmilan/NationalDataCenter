# Generated by Django 2.1.7 on 2019-12-11 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0001_initial'),
        ('Federal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='related_ministry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='offices.ExecutiveOffice'),
        ),
    ]
