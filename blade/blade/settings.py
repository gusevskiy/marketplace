import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d^y@9-3#2@ry#8!x@qkdat7+y^49pk3u0dcpa_7=7buvby4lrh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '*', 'localhost', '0.0.0.0']

CSRF_TRUSTED_ORIGINS = [
    "https://*.zrok.io",
]


# Application definition

INSTALLED_APPS = [
    'payment.apps.PaymentConfig',
    'product.apps.ProductConfig',
    'orders.apps.OrdersConfig',
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
    'cart.apps.CartConfig',
    'fontawesomefree',  # иконки
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blade.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        # после дебага изменить на True
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                # В переводе на человеческий язык эта инструкция будет звучать так:
                # Найди в корне проекта папку core/, в ней - папку context_processors/, там - файл year.py, а в этом файле - функцию year() Словарь, который она возвращает, добавь на все страницы проекта.
                'core.context_processors.year.year'
            ],
            # после дебага удалить
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
            # # после дебага удалить
            # 'debug': True
        },
    },
]

# # после дебага удалить
# THUMBNAIL_DEBUG = True
# THUMBNAIL_CACHE = 'default'


WSGI_APPLICATION = 'blade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'product:product_list'
LOGOUT_REDIRECT_URL = 'product:product_list'

CART_SESSION_ID = 'cart'

# Текст письма прилетает в консоль
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#  подключаем движок filebased.EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# указываем директорию, в которую будут складываться файлы писем
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')


CELERY_BROKER_URL = 'amqp://gusevskiy:Dreamer3190506@localhost:5672//'

broker_connection_retry_on_startup = True


# Ю-Касса
YOOKASSA_SECRET_KEY = os.getenv('YOOKASSA_SECRET_KEY')
YOOKASSA_SHOP_ID = os.getenv('YOOKASSA_SHOP_ID')