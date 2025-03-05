import os
from django.core.files import File
from django.core.management.base import BaseCommand
from product.models import Product, ProductImage


class Command(BaseCommand):
    """
    загрузить тестовые данные, доп параметром указать путь к папке с фотографиями
    название фотографии 1.jpg привязывается к id=1 и т.д.
    
    linux
    python manage.py load_images /mnt/c/Users/SuperBest/Pictures/ножи/
    windows
    python manage.py load_images C:\\Users\\SuperBest\\Pictures\\ножи
    """
    help = "Загрузка тестовых изображений и привязка их к продуктам"

    def add_arguments(self, parser):
        parser.add_argument('image_folder',
                            type=str,
                            help="Путь к папке с изображениями")

    def handle(self, *args, **kwargs):
        image_folder = kwargs['image_folder']

        # Проверяем, существует ли папка
        if not os.path.exists(image_folder):
            self.stdout.write(
                self.style.ERROR(f"Папка {image_folder} не существует"))
            return

        # Перебираем файлы в папке
        for file_name in os.listdir(image_folder):
            if file_name.endswith(
                ('.jpg', '.jpeg', '.png')):  # Проверяем формат
                # Получаем ID продукта из имени файла (например, 1.jpg → id=1)
                product_id = os.path.splitext(file_name)[0]
                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Продукт с id={product_id} не найден"))
                    continue

                # Путь к файлу изображения
                image_path = os.path.join(image_folder, file_name)

                # Создаем запись в модели ProductImage
                with open(image_path, 'rb') as img_file:
                    ProductImage.objects.create(product=product,
                                                image=File(img_file,
                                                           name=file_name))
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Изображение {file_name} привязано к продукту id={product_id}"
                    ))

        self.stdout.write(self.style.SUCCESS("Загрузка изображений завершена"))
