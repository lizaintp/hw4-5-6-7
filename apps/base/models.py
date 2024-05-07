from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='settings_logo/',
        verbose_name = 'Логотип'
    )
    fullname = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    subdescription = models.TextField(
        verbose_name='Миниописание'
    )
    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'

class Title(models.Model):
    desc = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    subdesc = models.CharField(
        max_length=255,
        verbose_name='Второе описание'
    )
    def __str__(self):
        return self.desc 
    
    class Meta:
        verbose_name = 'Главное описание'
        verbose_name_plural = 'Главные описания'
