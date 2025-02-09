# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordChangeView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordChangeDoneView
from django.views.generic import TemplateView
from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    # Вход
    # Полный адрес страницы регистрации - auth/signup/,
    # но префикс auth/ обрабатывется в головном urls.py
    path('signup/', views.SignUp.as_view(), name='signup'),

    # Выход
    # Что сдесь происходит: при клике на url 'users:logout' пользователь выходит из сессии и перенаправляется на след представление users:logged_out, а logged_out/ в свою очередь перенаправляет через встроенный класс TamplateView на страницу 'users/logged_out.html'. Хз по чему это не работает сразу из LogoutView.
    path('logout/', LogoutView.as_view(next_page='users:logged_out'), name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='users/logged_out.html'),
         name='logged_out'),

    # Регистрация
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),

    # Смена пароля
    path(
        'password_change/', PasswordChangeView.as_view(
            template_name='users/password_change_form.html'
        ), name='password_change_form'
    ),
    # Сообщение об успешном изменении пароля
    path(
        'password_change/done/', PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ), name='password_change_done'
    ),
    # Восстановление пароля
    path(
        'password_reset/', PasswordResetView.as_view(
            template_name='users/password_reset_form.html'),
        name='password_reset_form'
    ),
    # Сообщение об отправке ссылки для восстановления пароля
    path(
        'password_reset/done/', PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ), name='password_reset_done'
    ),
    # Вход по ссылке для восстановления пароля
    path(
        'reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
        ),
        name='password_reset_confirm'
    ),
    # Сообщение об успешном восстановлении пароля
    path(
        'reset/done/', PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ), name='password_reset_complete'
    ),

    path(
        'privacy-policy', TemplateView.as_view(
            template_name='users/privacy.html'
        ), name='privacy-policy'
    ),
]
