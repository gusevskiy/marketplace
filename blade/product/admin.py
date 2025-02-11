from django.contrib import admin
from .models import Product, Category, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.StackedInline):
  model = ProductImage
  max_num = 10
  extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'slug', 'price',
                    'available', 'created_at', 'updated_up']
    list_filter = ['available', 'created_at', 'updated_up']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    # Обязательное поле для работы autocomplete_fields
    search_fields = ('id', 'name')
    inlines = [ProductImageInline, ]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    # Отображение ID и связанных данных
    list_display = ('id', 'product', 'image')
    # Поиск по ID и названию товара
    search_fields = ('product__id', 'product__name')
    autocomplete_fields = ('product',)  # Автодополнение для выбора товара
