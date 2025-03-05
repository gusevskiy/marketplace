from django.db import models

class CDEKToken(models.Model):
    """
    access_token - токен
    expires_at - время истечение токена в секундах
    """
    access_token = models.CharField(max_length=255)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"CDEK Token (expires at {self.expires_at})"