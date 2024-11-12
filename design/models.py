from audioop import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Имя пользователя', unique=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    email = models.EmailField(max_length=254, verbose_name='Адрес электронной почты', unique=True)
    password = models.CharField(max_length=150, verbose_name="Пароль")

    GENDER_CHOICES = [
        ('M', "Мужчина"),
        ('F', "Женщина")
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Пол",
        default='M'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=150, help_text="Название категории")

    CATEGORY_CHOICES = [
        ('L', 'Лофт'),
        ('M', 'Минимализм'),
        ('K', "Классицизм"),
        ('A', 'Арт-деко'),
        ('H', 'Хай-тек'),
        ('O', "Не указано")
    ]

    def __str__(self):
        return self.name

class Application(models.Model):
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", )
    title = models.CharField(max_length=150, verbose_name="Название заявки")
    description = models.TextField(max_length=150, verbose_name="Описание заявки")
    image = models.FileField(upload_to=applicant, verbose_name="Загрузите фото заявки")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория заявки', default='O')

    STATUS_CHOICES = [
        ('N', "Новая"),
        ('P', "Принято в работу"),
        ('D', 'Выполнено')
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="N", verbose_name='Статус заявки')
    date = models.DateTimeField(help_text="Дата создания заявки", auto_now_add=True)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])

    def display_category(self):
        return self.category.name if self.category else "Категории нету"

    def __str__(self):
        return self.title

    display_category.short_description = 'Category'