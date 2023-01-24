# Generated by Django 4.1.5 on 2023-01-23 16:39

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0006_request_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='auto_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]
