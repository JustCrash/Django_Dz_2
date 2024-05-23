from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=40, verbose_name="Номер телефона", **NULLABLE, help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="Страна", **NULLABLE)

    verification_code = models.CharField(max_length=100, verbose_name="код", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
