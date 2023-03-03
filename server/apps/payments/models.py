from django.db import models
from apps.users.models import User
from apps.orders.models import Order
# Create your models here.
PAYMENT_STATUS = (
    (0, 'Failed'),
    (1, 'Success')
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_user')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments_order')
    amount = models.FloatField(null=True, blank=True)
    partnerName = models.CharField(max_length=30, null=True, blank=True)
    partnerId = models.CharField(max_length=11, null=True, blank=True)
    phoneUser = models.CharField(max_length=11, null=True, blank=True)
    comment = models.CharField(max_length=30, null=True, blank=True)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS, default=1)
    created = models.DateTimeField(auto_now_add=True)
    
