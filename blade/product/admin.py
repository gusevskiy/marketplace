from django.contrib import admin
from .models import Product, Category, ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    search_fields = ('id', 'name')  # Обязательное поле для работы autocomplete_fields

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'url')  # Отображение ID и связанных данных
    search_fields = ('product__id', 'product__name')  # Поиск по ID и названию товара
    autocomplete_fields = ('product',)  # Автодополнение для выбора товара

admin.site.register(Category)
