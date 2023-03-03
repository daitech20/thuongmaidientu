from rest_framework import serializers
from apps.orders.models import Cart, Order, OrderItem
from apps.products.api.serializers import ProductListSerializer

class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        if Cart.objects.filter(product=validated_data["product"]).exists():
            cart = Cart.objects.filter(product=validated_data["product"])[0]
            cart.quantity += validated_data["quantity"]
            cart.save()
            return cart
        
        else:
            return Cart.objects.create(**validated_data)    

class CartListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    product = ProductListSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        total_price = 0
        for cart in Cart.objects.filter(user=order.user):
            OrderItem.objects.create(order=order, quantity=cart.quantity, product=cart.product, price=cart.product.price * cart.quantity)
            total_price += cart.product.price * cart.quantity
        Cart.objects.all().delete()        
        order.total_price = total_price
        order.save()
        
        return order
