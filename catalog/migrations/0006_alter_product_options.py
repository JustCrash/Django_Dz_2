# Generated by Django 4.2.2 on 2024-06-02 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_options_product_owner_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category", "purchase_price"],
                "permissions": [
                    (
                        "cancellation_of_publication",
                        "Canceling the publication of the product",
                    ),
                    (
                        "changes_the_description",
                        "Changes the description of any product",
                    ),
                    ("changes_the_category", "Changes the category of any product"),
                    (
                        "may_cancel_the_publication_product",
                        "may cancel the publication product",
                    ),
                    ("can_edit_description_product", "Can edit description product"),
                    ("can_change_category_product", "Can change category product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
