# Generated by Django 2.2 on 2019-12-01 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='uploads/img', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png'])]),
        ),
    ]
