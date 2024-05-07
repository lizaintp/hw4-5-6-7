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

