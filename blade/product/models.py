from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    description = models.TextField(
        blank=True,  # Разрешаем оставить поле пустым в админке
        null=True,  # Разрешаем значение null
        verbose_name="Описание категории",
    )
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание товара"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Кол-во на складе")
    category = models.ForeignKey(
        Category,
        null=True,  # Разрешаем значение null
        blank=True,  # Разрешаем оставить поле пустым в админке
        related_name="product",
        on_delete=models.SET_DEFAULT,
        default=1,
    )
    brand = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Бренд"
    )
    material = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Материал лезвия"
    )
    blade_length = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Длина лезвия (см)",
    )
    handle_material = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Материал рукоятки"
    )
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Вес (г)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    updated_up = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"ID: {self.id} | {self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Товар"
    )
    url = models.ImageField(upload_to="product_images/", verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.product.name}"
