from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        max_length=300, verbose_name="Описание", help_text="Напишите описание категории"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        max_length=300, verbose_name="Описание", help_text="Напишите описание товара"
    )
    image = models.ImageField(
        upload_to="catalog/",
        verbose_name="Изображение",
        help_text="Вставъте изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Укажите категорию товара",
        related_name="products",
    )
    purchase_price = models.IntegerField(
        max_length=50, verbose_name="Цена", help_text="Укажите цену за покупку товара"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания товара",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "purchase_price"]
