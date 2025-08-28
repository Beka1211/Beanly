from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('payment/<int:pk>/', views.pay_order, name='payment'),
    path('order-items/', views.OrderItemListView.as_view(), name='orderitem-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailView.as_view(), name='orderitem-detail')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
