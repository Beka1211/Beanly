from django.db import models
from django.conf import settings
from shop.models import Product  # Бектемир


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Клиент",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("Дата заказа", auto_now_add=True)
    status = models.CharField(
        "Статус заказа",
        max_length=20,
        choices=[
            ("pending", "В обработке"),
            ("paid", "Оплачен"),
            ("shipped", "Доставлен"),
        ],
        default="pending"
    )

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
        return f"{self.quantity} × {self.product.name}"
