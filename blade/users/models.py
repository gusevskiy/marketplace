from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now


User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agreed_to_privacy = models.BooleanField(default=False)
    consent_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - {'Согласен' if self.agreed_to_privacy else 'Не согласен'}"