# Generated by Django 5.0.4 on 2024-05-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Напишите заголовок",
                        max_length=255,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        help_text="Вставте ссылку",
                        max_length=255,
                        null=True,
                        verbose_name="Ссылка",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Напишите содержание", verbose_name="Содержание"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Вставте изображение",
                        null=True,
                        upload_to="catalog/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Укажите дату создания",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "publication_sing",
                    models.BooleanField(default=True, verbose_name="Опубликовать"),
                ),
                (
                    "number_of_views",
                    models.IntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Напишите описание категории",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Напишите описание товара",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Вставъте изображение товара",
                null=True,
                upload_to="catalog/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="purchase_price",
            field=models.IntegerField(
                help_text="Укажите цену за покупку товара", verbose_name="Цена"
            ),
        ),
    ]
