from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должен быть email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None  # Убираем username
    email = models.EmailField(
        verbose_name="адрес email",
        max_length=254,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=150
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=150
    )

    agreed_to_privacy = models.BooleanField(default=False)
    consent_data  = models.DateTimeField(default=now)

    USERNAME_FIELD = 'email'  # Теперь логинимся по email
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()  # Подключаем кастомный менеджер

    def __str__(self):
        return f"{self.get_full_name()} - {'Согласен' if self.agreed_to_privacy else 'Не согласен'}"
