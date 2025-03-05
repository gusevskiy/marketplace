import logging
from celery import shared_task
from django.utils import timezone
from .models import Cache

logger = logging.getLogger(__name__)


@shared_task
def clear_expired_cache_task():
    """Задача Celery для очистки устаревшего кэша."""
    try:
        count = Cache.objects.filter(expire_at__lt=timezone.now()).delete()[0]
        logger.info(f"Cleared {count} expired cache entries")
        return f"Cleared {count} expired cache entries"
    except Exception as e:
        logger.error(f"Error clearing expired cache: {e}")
        return f"Error clearing expired cache: {e}"