from django.db import models

# Create your models here.
class Blog(models.Model):
    autor = models.CharField(
        max_length=255, 
        verbose_name='Автор',
        help_text='Нужно написать автора блога'
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    title = models.CharField(
        max_length=600,
        verbose_name='Название блога'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение поста'
    )
    def __str__(self):
        return self.autor
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

class FacultyDirectory(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Имя'
    )
    profession = models.CharField(
        max_length=600,
        verbose_name='Профессия'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'

class Info(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name ='Имя'
    )
    profession = models.CharField(
        max_length=600,
        verbose_name = 'Профессия'
    )
    image = models.ImageField(
        upload_to = 'image/',
        verbose_name ='Фото'
    )
    email = models.EmailField(
        verbose_name ='Почта'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name ='Телефон'
    )
    desc = models.TextField(
        verbose_name ='Описание'
    )
    bio = models.CharField(
        max_length=255, 
        verbose_name ='Биография'
    )
    desceducation = models.TextField(
        verbose_name ='Описание образавания'
    )
    areasofexpertise = models.TextField(
        verbose_name ='Области специализации'
    )
    publication = models.TextField(
        verbose_name ='Публикация'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Информация о факультете'
        verbose_name_plural = 'Информации о факультете'

class Event(models.Model):
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
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'   



class Alumni(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
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
        verbose_name = 'Выпускник'
        verbose_name_plural = 'Выпускники'