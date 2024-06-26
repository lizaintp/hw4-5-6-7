# Generated by Django 5.0.4 on 2024-05-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_alumni'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusLive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Кампус',
                'verbose_name_plural': 'Кампусы',
            },
        ),
    ]
