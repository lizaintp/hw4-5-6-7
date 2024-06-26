# Generated by Django 5.0.4 on 2024-05-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0011_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Ученый',
                'verbose_name_plural': 'Ученые',
            },
        ),
    ]
