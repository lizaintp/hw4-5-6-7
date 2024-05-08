# Generated by Django 5.0.4 on 2024-05-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0010_artculture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Спорт',
                'verbose_name_plural': 'Спорт',
            },
        ),
    ]