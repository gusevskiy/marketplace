import pandas as pd
import numpy as np

# Создаем данные для CSV
np.random.seed(42)  # Для воспроизводимости результатов

# Списки возможных значений для каждого столбца
name = [f"Нож {i}" for i in range(1, 51)]
description = [f"Описание ножа {i}" for i in range(1, 51)]
price = np.random.randint(500, 5000, 50)  # Случайные цены от 500 до 5000
stock = np.random.randint(1, 100, 50)  # Случайное количество от 1 до 100
category = np.random.choice(["Рыбалка", "Охота", "Кухонные"], 50)
brand = np.random.choice(["Кузница A", "Кузница B", "Кузница C", "Кузница D"], 50)
material = np.random.choice(["Нержавеющая сталь", "Углеродистая сталь", "Дамаск"], 50)
blade_length = np.random.uniform(5, 15, 50).round(1)  # Случайная длина от 5 до 15 см
handle_material = np.random.choice(["Дерево", "Пластик", "Резина", "Металл"], 50)
weight = np.random.uniform(50, 300, 50).round(1)  # Случайный вес от 50 до 300 грамм

# Создаем DataFrame
data = {
    "name": name,
    "description": description,
    "price": price,
    "stock": stock,
    "category": category,
    "brand": brand,
    "material": material,
    "blade_length": blade_length,
    "handle_material": handle_material,
    "weight": weight
}

df = pd.DataFrame(data)

# Сохраняем DataFrame в CSV файл
df.to_csv("blade.csv", index=False, encoding="utf-8-sig")

print("Файл 'ножи.csv' успешно создан!")