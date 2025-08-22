from django.db import models
from shop.models import Product  # Бектемир
from users.models import MyUser # Bektemir


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField("Email клиента")
    phone = models.CharField("Телефон", max_length=30, blank=True)
    created_at = models.DateTimeField("Дата заказа", auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    payment_transaction_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.id} от {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name="Заказ",
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        verbose_name="Позиция",
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField("Количество", default=1)

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return f"{self.quantity} × {self.product.title}"

