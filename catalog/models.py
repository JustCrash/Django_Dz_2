from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Напишите описание категории"
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
        **NULLABLE, verbose_name="Описание", help_text="Напишите описание товара"
    )
    image = models.ImageField(
        **NULLABLE,
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
        verbose_name="Цена",
        help_text="Укажите цену за покупку товара",
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


class Contacts(models.Model):
    city = models.CharField(max_length=50, verbose_name="Страна")
    identity_nalog_number = models.IntegerField(verbose_name="ИНН")
    address = models.TextField(verbose_name="Адрес")
    slug = models.CharField(max_length=255, verbose_name="URL", **NULLABLE)

    def __str__(self):
        return f"{self.city} {self.identity_nalog_number} {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class BlogPost(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Напишите заголовок",
    )
    slug = models.CharField(
        max_length=255,
        verbose_name="Ссылка",
        **NULLABLE,
        help_text="Вставте ссылку",
    )
    content = models.TextField(
        verbose_name="Содержание",
        help_text="Напишите содержание",
    )
    preview = models.ImageField(
        upload_to="catalog/",
        verbose_name="Изображение",
        help_text="Вставте изображение",
        **NULLABLE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    publication_sing = models.BooleanField(
        default=True,
        verbose_name="Опубликовать",
    )
    number_of_views = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    number_of_version = models.PositiveIntegerField(
        verbose_name="Номер версии продукта",
    )
    name_of_versions = models.CharField(
        max_length=150,
        verbose_name="Название версии",
    )
    is_active_version = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
