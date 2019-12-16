# Generated by Django 2.1.7 on 2019-12-12 09:39

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Federal', '0020_remove_executive_related_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legislative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('related_file', models.FileField(blank=True, upload_to='files/')),
                ('is_published', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='leg_last_modified_by', to=settings.AUTH_USER_MODEL)),
                ('related_house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='offices.LegislativeOffice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='executive',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ex_last_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
