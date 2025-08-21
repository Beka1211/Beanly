from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


# Список заказов и создание нового заказа (только для авторизованных)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # только авторизованные могут видеть/создавать

# Детальный просмотр: нужен для того, чтобы редактировать и удалять конкретный заказ
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # только авторизованные могут редактировать/удалять 
