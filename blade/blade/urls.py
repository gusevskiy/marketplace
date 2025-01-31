from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django проверяет url-адреса сверху вниз,
    # нам нужно, чтобы Django сначала проверял адреса в приложении users
    path('auth/', include('users.urls', namespace="users")),
    # Если какой-то URL не обнаружится в приложении users —
    # Django пойдёт искать его в django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('cart/', include('cart.urls', namespace='cart')),

    path('orders/', include('orders.urls', namespace='orders')),

    path("", include('product.urls', namespace='product')),
]

if settings.DEBUG:  # Для разработки
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
