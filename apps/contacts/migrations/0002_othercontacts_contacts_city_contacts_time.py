# Generated by Django 5.0.4 on 2024-05-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(help_text='Нужно описание кампус', verbose_name='Описание')),
                ('phone', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Другой контакт в кампусе',
                'verbose_name_plural': 'Другие контакты в кампусе',
            },
        ),
        migrations.AddField(
            model_name='contacts',
            name='city',
            field=models.CharField(default=1, max_length=255, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='time',
            field=models.CharField(default=1, help_text='Нужно написать график в какие дни, со скольки до скольки отвечаете', max_length=255, verbose_name='График'),
            preserve_default=False,
        ),
    ]
