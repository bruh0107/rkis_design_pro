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
        ('F', "Женщина"),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Пол",
        default='M'
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username