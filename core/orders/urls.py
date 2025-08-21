from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
