from django.db import models
from django.utils import timezone

class Cache(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    expire_at = models.DateTimeField(null=True, blank=True)

    def is_expired(self):
        return self.expire_at and timezone.now() > self.expire_at

    def __str__(self):
        return self.key
