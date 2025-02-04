# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView
from django.views.generic import TemplateView
from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    # Полный адрес страницы регистрации - auth/signup/,
    # но префикс auth/ обрабатывется в головном urls.py
    path('signup/', views.SignUp.as_view(), name='signup'),



    path('logout/', LogoutView.as_view(next_page='users:logged_out'), name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='users/logged_out.html'),
         name='logged_out'),

    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    # Восстановление пароля
    path(
        'password_reset/', PasswordResetView.as_view(
            template_name='users/password_reset_form.html'),
        name='password_reset_form'
    ),
]
