# Generated by Django 4.1.5 on 2023-01-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0010_alter_post_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]