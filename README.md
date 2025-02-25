## marketplace

### Pet проект в разработке

разработка на django 5, на фронте bootstrap (задача не использовать JS)

на текущий момент реализовано

- аунтификация по email с мгновенной авторизацией
- аунтификация с пометкой на согласие обработки персональных данных
- корзина товаров
- оповещение покупателя о заказе на почту (selery)
- оплата товаров (юкасса тестовый магазин)

Глобальные.

- Social authenticate
- CDEK
- CRM

note (мысли):

1. подпись в footer.html
2. Корзина
3. Валидация вводимых значений
4. Статичные страницы для футера
5. Добавление в корзину из product_list с карточек
6. одну кнопку оставить войти может убрать слово регистрация
7. количество товаров в корзине на значке (как у ozon)
8. добавление в корзину из карточек, без перехода к товару
9. компоновка форм
10. перепроверить толи соглашение разместил на сайте

## Start

```bash
git clone
. venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
# download data
python manage.py load_product
windows
python manage.py load_images C:\\Users\\SuperBest\\Pictures\\ножи
ubuntu
python3 manage.py load_images /home/gusevskiy/windows/ножи

# RabbitMQ
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
# Celery
celery -A blade worker -l info
```

Снести БД:

```bash
# удалить миграции
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
# Удалить бд
rm db.sqlite3
# Создать БД заново (применить миграции)
python manage.py makemigrations
 python manage.py migrate
```

https://github.com/PacktPublishing/Django-4-by-Example/tree/main/Chapter08/myshop/shop/static

https://htmx.org/docs/#installing

https://tailwindcss.com/

# bootstrap

https://getbootstrap.su/ # на русском
https://getbootstrap.su/docs/5.3/utilities/background/ # цвета
https://getbootstrap.su/docs/5.3/utilities/flex/ # центрирование

# расшифровка классов

https://getbootstrap.com/docs/5.3/utilities/spacing/

## Шрифты google

https://fonts.google.com/selection/embed

## Иконки

https://fontawesome.com/icons
https://docs.fontawesome.com/web/use-with/python-django

Test
запустить все тесту cart
python manage.py test cart.tests.CartTests.

какой то один
python manage.py test cart.tests.CartTests.test_add_product
