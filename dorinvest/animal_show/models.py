from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Show(models.Model):
    """Основная информация о выставке животных"""
    CAT = 'cat'
    DOG = 'dog'
    ANIMALS_CHOICES = [
        ("cat", "кошка"),
        ("dog", "собака"), ]

    title = models.CharField(max_length=255, verbose_name='Название выставки')
    banner = models.ImageField(upload_to='banner/',  verbose_name='Баннер')
    info = models.TextField(verbose_name='Информация о выставке')
    logo = models.ImageField(upload_to='logo/', verbose_name='Логотипы партнеров')
    contacts = models.TextField(verbose_name='Контакты')
    last_images = models.ImageField(upload_to='last_images/', verbose_name='Фотография животных с прошлой выставки')
    date = models.DateField(verbose_name='Дата проведения')
    location = models.CharField(max_length=255, verbose_name='Место проведения')
    social_links = models.URLField(verbose_name='Ссылки на социальные сети')

    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    result_images = models.ImageField(upload_to='result_images/',  verbose_name='Фотография животных по завершению выставки')
    result = models.TextField(verbose_name='Итоги выставки')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    animals = models.ImageField(upload_to='animals/', verbose_name='Фотография животных')
    description = models.TextField(verbose_name='Описание животного')
    category = models.CharField(max_length=3, choices=ANIMALS_CHOICES, verbose_name='Категория животного')

    def __str__(self):
        return f"{self.title} {self.description} ({self.category})"



# class Animals(models.Model):
#     """Информация о животных, участвующих в выставке"""
#     CAT = 'cat'
#     DOG = 'dog'
#     ANIMALS_CHOICES = [
#         ("cat", "кошка"),
#         ("dog", "собака"),]
#     animals = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='animals')
#     image = models.ManyToManyField('Image', related_name='image',  verbose_name='Фотография животных')
#     description = models.TextField(verbose_name='Описание животного')
#     category = models.CharField(max_length=3, choices=ANIMALS_CHOICES, verbose_name='Категория животного')
#
#     def __str__(self):
#         return f"{self.description} ({self.category})"
#
#
# class Image(models.Model):
#     images = models.ImageField(upload_to='images/', verbose_name='Изображения')
