import json
from datetime import timedelta
from django.utils import timezone
from .models import Cache

def cache_set(key, value, timeout=None):
    expire_at = timezone.now() + timedelta(seconds=timeout) if timeout else None
    Cache.objects.update_or_create(
        key=key,
        defaults={'value': json.dumps(value), 'expire_at': expire_at}
    )

def cache_get(key):
    try:
        cache_obj = Cache.objects.get(key=key)
        if not cache_obj.is_expired():
            return json.loads(cache_obj.value)
        else:
            cache_obj.delete()
            return None
    except Cache.DoesNotExist:
        return None

def cache_delete(key):
    Cache.objects.filter(key=key).delete()