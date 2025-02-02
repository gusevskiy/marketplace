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




Test
запустить все тесту cart
python manage.py test cart.tests.CartTests.

какой то один 
python manage.py test cart.tests.CartTests.test_add_product





Тeстовые пользователи
petrov
vlgu12@yandex.ru