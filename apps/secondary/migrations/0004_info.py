# Generated by Django 5.0.4 on 2024-05-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0003_facultydirectory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('profession', models.CharField(max_length=600, verbose_name='Профессия')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('bio', models.CharField(max_length=255, verbose_name='Биография')),
                ('desceducation', models.TextField(verbose_name='Описание образавания')),
                ('areasofexpertise', models.TextField(verbose_name='Области специализации')),
            ],
            options={
                'verbose_name': 'Информация о факультете',
                'verbose_name_plural': 'Информации о факультете',
            },
        ),
    ]