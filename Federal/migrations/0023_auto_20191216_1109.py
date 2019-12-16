# Generated by Django 2.1.7 on 2019-12-16 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('Federal', '0022_judiciary'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category'),
        ),
        migrations.AddField(
            model_name='judiciary',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category'),
        ),
        migrations.AddField(
            model_name='legislative',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category'),
        ),
    ]
