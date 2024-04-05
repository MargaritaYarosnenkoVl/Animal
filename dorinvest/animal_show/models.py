from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models



class Show(models.Model):
    """Основная информация о выставке животных"""

    title = models.CharField(max_length=255, verbose_name='Название выставки')
    banner = RichTextField(verbose_name='Баннер')
    info = models.TextField(verbose_name='Информация о выставке')
    logo = RichTextField(verbose_name='Логотипы партнеров')
    contacts = models.TextField(verbose_name='Контакты')
    last_images = RichTextField(verbose_name='Фотография животных с прошлой выставки')
    date = models.DateField(verbose_name='Дата проведения')
    location = models.CharField(max_length=255, verbose_name='Место проведения')
    social_links = models.URLField(verbose_name='Ссылки на социальные сети')

    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    result_images = RichTextField(blank=True, null=True, verbose_name='Фотография животных по завершению выставки')
    result = models.TextField(blank=True, null=True, verbose_name='Итоги выставки')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    animals = models.ManyToManyField('Animals', related_name='animals', verbose_name='Животные')

    # animals = RichTextField(verbose_name='Фотография животных')
    # description = models.TextField(verbose_name='Описание животного')
    # category = models.CharField(max_length=3, choices=ANIMALS_CHOICES, verbose_name='Категория животного')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f'/{self.id}'



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

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_absolute_url(self):
        return f'/{self.id}'

class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    email = models.EmailField(max_length=255, verbose_name='Электронный адрес (email)')
    content = models.TextField(verbose_name='Содержимое письма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя',  blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        db_table = 'app_feedback'

    def __str__(self):
        return f'Вам письмо от {self.email}'