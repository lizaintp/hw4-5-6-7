from django.db import models

# Create your models here.
class Contacts(models.Model):
    city = models.CharField(
        max_length=255,
        verbose_name='Город'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Местоположение'
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефон номера'
    )
    time = models.CharField(
        max_length=255,
        verbose_name='График',
        help_text='Нужно написать график в какие дни, со скольки до скольки отвечаете'
    )
    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class OtherContacts(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Нужно описание кампус'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name = 'Задний фон'
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Другой контакт в кампусе'
        verbose_name_plural = 'Другие контакты в кампусе'
