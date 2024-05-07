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

class Student(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Программа',
        help_text='Вам нужно написать программу которая ведется у студента'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Программа студента'
        verbose_name_plural = 'Программы студента'

class Graduate(models.Model):
    name = models.CharField(
    max_length=255,
    verbose_name='Программа',
    help_text='Вам нужно написать программу которая ведется у выпускника'
)
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Программа выпускника'
        verbose_name_plural = 'Программы выпускника'

class LifelongLearning(models.Model):
    name = models.CharField(
    max_length=255,
    verbose_name='Программа',
    help_text='Вам нужно написать программу которая ведется на протяжении всей жизни'
)
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Обучение всей жизни'
        verbose_name_plural = 'Обучения всей жизни'

class LifeinCampus(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название студентеческой жизни'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Жизнь в кампусе'
        verbose_name_plural = 'Жизнь в кампусах'