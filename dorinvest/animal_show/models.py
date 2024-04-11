from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Show(models.Model):
    """Основная информация о выставке животных"""
    title = models.CharField(max_length=255, verbose_name='Название выставки')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    info = models.TextField(verbose_name='Информация о выставке')
    quantity = models.CharField(max_length=255, verbose_name='Информация о количестве животных')
    organizer = models.CharField(max_length=255, verbose_name='Информация об организаторе')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')


    animals = models.ManyToManyField('Animals', related_name='animals', verbose_name='Животные')
    banners = models.ManyToManyField('Banner', related_name='banners', verbose_name='Баннер')
    stores = models.ManyToManyField('Story', related_name='stores', verbose_name='Счастливые истории')
    locations = models.ManyToManyField('Location', related_name='locations', verbose_name='Место проведения')
    social_links = models.ManyToManyField('SociaLinks', related_name='social_links', verbose_name='Ссылки на социальные сети')
    partners = models.ManyToManyField('Partners', related_name='partners', verbose_name='Ссылки на страницу партнера')

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ['id']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('show', kwargs={'slug': self.slug})




class Animals(models.Model):
    """Информация о животных, участвующих в выставке"""
    CAT = 'cat'
    DOG = 'dog'
    ANIMALS_CHOICES = [
        ("cat", "кошка"),
        ("dog", "собака"),]

    image_animals = models.ImageField(upload_to='images/', verbose_name='Фотография животного')
    name = models.CharField(max_length=255, verbose_name='Имя животного')
    description = models.TextField(verbose_name='Описание животного')
    category = models.CharField(max_length=3, choices=ANIMALS_CHOICES, verbose_name='Категория животного')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_absolute_url(self):
        return f'/{self.id}'


class Feedback(models.Model):
    """
    Модель обратной связи
    """
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    user_phone = models.CharField(max_length=25, verbose_name='Телефон пользователя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['id']
        # db_table = 'app_feedback'

    def get_absolute_url(self):
        return f'/{self.slug}'


class Banner(models.Model):
    """Модель, содержащая иображение баннера"""
    name = models.CharField(max_length=255, verbose_name='Название баннера')
    banner = models.ImageField(upload_to='baner/', verbose_name='Банер')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"


class Story(models.Model):
    """ Счастливые истории"""
    name = models.CharField(max_length=255, verbose_name='Имя животного, которого забрали')
    story = models.CharField(max_length=255, verbose_name='История пристройства')
    photo = models.ImageField(upload_to='story/', verbose_name='Фотография пристроенного животного')

    class Meta:
        verbose_name = 'Счастливые истории'
        verbose_name_plural = 'Счастливые истории'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    """ Как к нам добраться"""
    place = models.CharField(max_length=255, verbose_name='Место проведения выставки')
    phone = models.CharField(max_length=25, verbose_name='Телефон организатора')
    duration = models.CharField(max_length=30, verbose_name='Время проведения мероприятия')

    class Meta:
        verbose_name = 'Как к нам добраться'
        verbose_name_plural = 'Как к нам добраться'
        ordering = ['id']

    def __str__(self):
        return f"{self.place}"


class SociaLinks(models.Model):
    """ Ссылки на социальные сети"""
    name = models.CharField(max_length=255, verbose_name='Название социальной сети')
    social_link = models.URLField(verbose_name='Ссылки на социальные сети')
    social_logo = models.ImageField(upload_to='social_links/', verbose_name='Логотип социальной сети')

    class Meta:
        verbose_name = 'Ссылки на социальные сети'
        verbose_name_plural = 'Ссылки на социальные сети'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"


class Partners(models.Model):
    """ Логотипы партнеров"""
    name = models.CharField(max_length=255, verbose_name='Название партнера')
    logo = models.ImageField(upload_to='partners/', verbose_name='Логотип партнеров')
    partners_link = models.URLField(verbose_name='Ссылка на страницу партнера')

    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"


class EndedShow(models.Model):
    """Прошедшая выставка"""
    title = models.CharField(max_length=255, verbose_name='Название выставки')
    image = models.ImageField(upload_to='EndedShow/', verbose_name='Фотография с выставки')
    date = models.DateField(verbose_name='Дата проведения выставки')
    count = models.CharField(max_length=50, verbose_name='Количество животных на выставке')
    animal_housing = models.CharField(max_length=50, verbose_name='Количество пристроенных животных')
    descriptions = models.TextField(verbose_name='Информация по прошедшей выставке')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    photoreport = models.ManyToManyField('Photoreport', related_name='photoreport', verbose_name='Фотоотчет с выставки')

    class Meta:
        verbose_name = 'Прошедшие выставки'
        verbose_name_plural = 'Прошедшие выставки'
        ordering = ['id']

    def __str__(self):
        return f"{self.title}"



class Photoreport(models.Model):
    """Фотоотчет"""
    photo = models.ImageField(upload_to='photoreport/', verbose_name='Фотоотчет с выставки')

    class Meta:
        verbose_name = 'фотоотчет'
        verbose_name_plural = 'фотоотчет'
        ordering = ['id']

    def __str__(self):
        return f"{self.photo}"




