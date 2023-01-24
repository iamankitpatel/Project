# Generated by Django 4.1.5 on 2023-01-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0008_post_date_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]
