from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('order/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
