from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField()