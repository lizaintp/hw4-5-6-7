# Generated by Django 5.0.4 on 2024-05-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_scholarships_remove_tuitionfees_subtitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятии')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('data', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('location', models.CharField(max_length=255, verbose_name='Местоположение')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
