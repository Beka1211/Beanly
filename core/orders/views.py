from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


@swagger_auto_schema(
    method='post',
    operation_description="Оплата заказа",
    responses={200: OrderSerializer()}
)
@api_view(['POST'])
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
