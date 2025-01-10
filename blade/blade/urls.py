from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    # Django проверяет url-адреса сверху вниз,
    # нам нужно, чтобы Django сначала проверял адреса в приложении users
    path('auth/', include('users.urls', namespace="users")),
    # Если какой-то URL не обнаружится в приложении users —
    # Django пойдёт искать его в django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),

    path("", include('product.urls', namespace='product')),
    path('admin/', admin.site.urls),
]
