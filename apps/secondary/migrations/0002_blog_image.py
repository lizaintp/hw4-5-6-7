# Generated by Django 5.0.4 on 2024-05-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='image/', verbose_name='Изображение поста'),
            preserve_default=False,
        ),
    ]
