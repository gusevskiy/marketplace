# marketplace
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


https://github.com/PacktPublishing/Django-4-by-Example/tree/main/Chapter08/myshop/shop/static


https://htmx.org/docs/#installing

https://tailwindcss.com/

# bootstrap
https://getbootstrap.su/  # на русском 
https://getbootstrap.su/docs/5.3/utilities/background/  # цвета

# расшифровка классов
https://getbootstrap.com/docs/5.3/utilities/spacing/
## Шрифты google
https://fonts.google.com/selection/embed
## Иконки
https://fontawesome.com/icons
https://docs.fontawesome.com/web/use-with/python-django

note:
1) подпись в footer.html
2) Корзина
3) Валидация вводимых значений
4) Статичные страницы для футера [ссылка](https://practicum.yandex.ru/learn/backend-developer/courses/1b78b2c9-df6f-4349-a831-7ef978dd092f/sprints/72332/topics/03b3895d-0391-4b6f-8247-8e6f5be17568/lessons/5679e3c2-82aa-4d36-b184-dfa794ed3a08/)
5) Добавление в корзину из product_list с карточек
6) одну кнопку оставить войти может убрать слово регистрация
7) количество товаров в корзине на значке (как у ozon)
8) добавление в корзину из карточек, без перехода к товару
9) компоновка форм




Test
запустить все тесту cart
python manage.py test cart.tests.CartTests.

какой то один 
python manage.py test cart.tests.CartTests.test_add_product





Тeстовые пользователи
petrov
vlgu12@yandex.ru