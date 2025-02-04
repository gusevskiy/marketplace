# users/views.py
# Импортируем CreateView, чтобы создать ему наследника
from ast import arg
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('product:product_list')
    template_name = 'users/signup.html'


# class CustomLogoutView(LogoutView):
#     """ Для реализации выхода из аккаунта (тк в django 5 LogoutView не принимает)"""
#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)