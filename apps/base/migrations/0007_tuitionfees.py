# Generated by Django 5.0.4 on 2024-05-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_lifeincampus'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('subtitle', models.TextField(verbose_name='тайтл')),
                ('name', models.CharField(max_length=255, verbose_name='Второе название')),
                ('subname', models.CharField(max_length=255, verbose_name='подтайтл')),
                ('list', models.CharField(max_length=255, verbose_name='Список программ бакалавриата')),
            ],
            options={
                'verbose_name': 'Плата за обучение',
                'verbose_name_plural': 'Платы за обучения',
            },
        ),
    ]