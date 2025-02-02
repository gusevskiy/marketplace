from tabnanny import verbose
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from django.conf import settings
from django.urls import reverse


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

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:product_list_by_category", args=[self.slug])
    

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание товара"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Кол-во на складе")
    category = models.ForeignKey(
        Category,
        null=True,  # Разрешаем значение null
        blank=True,  # Разрешаем оставить поле пустым в админке
        related_name="products",
        on_delete=models.SET_DEFAULT,
        default=1,
    )
    slug = models.SlugField(max_length=200)
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
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления")
    updated_up = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменения")
    # наличие товара
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),  # - дефис для обратной сортировки
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id, self.slug])
    

    def __str__(self):
        return f"ID: {self.id} | {self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Товар"
    )
    image = models.ImageField(upload_to="product_images/", blank=True,
                            verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.product.name}"
