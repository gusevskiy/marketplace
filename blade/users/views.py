# users/views.py
# Импортируем CreateView, чтобы создать ему наследника
from ast import arg
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.template.loader import render_to_string
from django.views.generic import TemplateView
import os
import markdown
from django.conf import settings

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


class PrivacyPolicyView(TemplateView):
    template_name = "users/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_path = os.path.join(settings.BASE_DIR, "data/privacy.md")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                context['privacy_policy_text'] = markdown.markdown(f.read())
        except FileNotFoundError:
            context['privacy_policy_text'] = "<p>Текст согласия временно недоступен.</p>"

        return context

