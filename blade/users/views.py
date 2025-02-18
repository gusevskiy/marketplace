from ast import arg
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.template.loader import render_to_string
from django.views.generic import TemplateView
import os
from django.contrib.auth import login, authenticate  # Импортируем функцию login
from datetime import datetime
import markdown
from django.conf import settings

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    # форма для создания объекта
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('product:product_list')
    # путь к шаблону
    template_name = 'users/signup.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['email'], password=cd['password1'])
        login(self.request, user)
        return result


class PrivacyPolicyView(TemplateView):
    """представление policy"""
    template_name = "users/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_path = os.path.join(settings.BASE_DIR, "data/privacy.md")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                context['privacy_policy_text'] = markdown.markdown(f.read())

            # Получаем дату последнего изменения файла
            last_modified_time = os.path.getmtime(file_path)
            context['last_modified'] = datetime.fromtimestamp(
                last_modified_time).strftime('%d %B %Y, %H:%M')
        except FileNotFoundError:
            context[
                'privacy_policy_text'] = "<p>Текст согласия временно недоступен.</p>"
            context['last_modified'] = None

        return context
