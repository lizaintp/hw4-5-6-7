# Generated by Django 5.0.4 on 2024-05-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_feedback_imageclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='profession',
            field=models.CharField(max_length=255, verbose_name='Профессия'),
        ),
    ]
