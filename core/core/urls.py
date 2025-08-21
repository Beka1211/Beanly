from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (     # JWT
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
]

if settings.DEBUG:   # правильное форматирование и меньше вероятность ошибок, используем этот вариант Бектемир)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
