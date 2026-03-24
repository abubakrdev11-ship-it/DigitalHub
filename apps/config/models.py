from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сайта")
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "1) Основные настройки"
        verbose_name_plural = "1) Основные настройки"

class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "2) Услуги"
        verbose_name_plural = "2) Услуги"