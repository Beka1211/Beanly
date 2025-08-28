from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    @swagger_auto_schema(
        operation_description="Получить список заказов текущего пользователя или создать новый заказ",
        responses={200: OrderSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новый заказ",
        responses={201: OrderSerializer()}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    @swagger_auto_schema(
        operation_description="Получить, обновить или удалить конкретный заказ",
        responses={200: OrderSerializer()}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@swagger_auto_schema(
    method='post',
    operation_description="Оплата заказа по ID",
    responses={200: OrderSerializer()}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])   # 👈 добавлено
def pay_order(request, pk):
    try:
        order = Order.objects.get(pk=pk, user=request.user)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    if order.status == 'paid':
        return Response({"error": "Already paid"}, status=400)

    order.status = 'paid'
    order.payment_transaction_id = f"TEST-{order.id}"
    order.save()

    return Response({
        "status": "success",
        "transaction_id": order.payment_transaction_id
    })


class OrderItemListView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return OrderItem.objects.all().select_related('order', 'product')
        return OrderItem.objects.filter(order__user=user).select_related('order', 'product')

    @swagger_auto_schema(
        operation_description="Получить список позиций заказов",
        responses={200: OrderItemSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderItemDetailView(generics.RetrieveAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return OrderItem.objects.all().select_related('order', 'product')
        return OrderItem.objects.filter(order__user=user).select_related('order', 'product')

    @swagger_auto_schema(
        operation_description="Получить детали позиции заказа",
        responses={200: OrderItemSerializer()}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
