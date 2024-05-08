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

class TuitionFees(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Тайтл'
    )
    subname = models.CharField(
        max_length=255,
        verbose_name='Подтайтл'
    )
    list = models.CharField(
        max_length=255,
        verbose_name='Список программ бакалавриата'
    )
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Плата за обучение'
        verbose_name_plural = 'Платы за обучения'

class Scholarships(models.Model):
    desc = models.TextField(
        verbose_name='Описание стипендии'
    )
    class Meta:
        verbose_name = 'Стипендия'
        verbose_name_plural = 'Стипендии'

class AlumniEvent(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название мероприятии'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    data = models.DateField(
        verbose_name='Дата'
    )
    time = models.TimeField(
        verbose_name='Время'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Местоположение'
    )
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Мероприятие для студента' 
        verbose_name_plural = 'Мероприятия для студентов'

class History(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self. title
    
    class Meta:
        verbose_name = 'История Университета'
        verbose_name_plural = 'Истории Университета'

class MissionValuesRight(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name="Подазвание"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self. title
    class Meta:
        verbose_name = 'Миссия и ценности левая часть'
        verbose_name_plural = 'Миссии и ценности левые части'

class MissionValuesLeft(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name="Подазвание"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self. title
    class Meta:
        verbose_name = 'Миссия и ценности правая часть'
        verbose_name_plural = 'Миссии и ценности правые части'

class OurCampusTour(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    video = models.URLField(
        verbose_name='Видео'
    )
    def __str__(self):
        return self. title
    class Meta:
        verbose_name = 'Экскурсия по кампусу'
        verbose_name_plural = 'Экскурсии по кампусу'

class Feedback(models.Model):
    autor = models.CharField(
        max_length =255,
        verbose_name ="Автор"
    )
    profession = models.CharField(
        max_length=255,
        verbose_name="Профессия"
    )
    feedback = models.TextField(
        verbose_name="Описание"
    )
    imageclient = models.ImageField(
        upload_to ='image/',
        verbose_name='Фото клиента'
    )
    image= models.ImageField(
        upload_to ='image/',
        verbose_name ='Фото Учителя'
    )
    def __str__(self):
        return self.autor
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


