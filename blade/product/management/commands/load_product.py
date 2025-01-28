import csv
from venv import create
from django.core.management.base import BaseCommand, CommandParser
from product.models import Product, Category


class Command(BaseCommand):
    """
    загрузить данные командой
    python manage.py load_product
    """
    def handle(self, *args, **kwargs):
        csv_file_path = r"C:\DEVELOP\marketplace\blade\data\blade.csv"
        self.stdout.write(self.style.WARNING("Старт команды"))
        with open(csv_file_path, mode="r", encoding="utf-8-sig") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.stdout.write(
                self.style.WARNING(
                    f"Заголовки CSV: {csv_reader.fieldnames}"
                )
            )
            for row in csv_reader:
                # Отладочный вывод строки
                self.stdout.write(self.style.NOTICE(f"Читаем строку: {row}"))

                category, create = Category.objects.get_or_create(
                    name=row['category'])

                Product.objects.get_or_create(
                    name=row['name'],
                    description=row['description'],
                    price=row['price'],
                    stock=row['stock'],
                    category=category,
                    brand=row['brand'],
                    material=row['material'],
                    blade_length=row['blade_length'],
                    handle_material=row['handle_material'],
                    weight=row['weight'],
                )
            self.stdout.write(self.style.SUCCESS("Данные загружены"))
