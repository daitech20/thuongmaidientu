from django.db import models
from apps.users.models import User
from apps.products.models import Product
from apps.profiles.models import Address

# Create your models here.
ORDER_STATUS = (
    (0, 'cancel'),
    (1, 'confirm'),
    (2, 'unconfimred'),
    (3, 'being transported'),
    (4, 'delivered')
)

PAYMENT_METHODS = (
    (0, 'cash'),
    (1, 'momo')
)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts_user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carts_product")
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product',)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders_user")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address_order")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=2)
    payment_method = models.IntegerField(choices=PAYMENT_METHODS, default=0)
    has_paid = models.BooleanField(default=False)

    def get_total_price(self):
        total = 0
        for order_item in self.orderitems_order.all():
            total += order_item.get_price()
        self.total_price = total
        return total

class OrderItem(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderitems_product")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderitems_order")
    price = models.FloatField(default=0)

    def get_price(self):
        return self.product.price * self.quantity