from rest_framework import permissions
from rest_framework import generics, status
from apps.orders.api.serializers import CartSerializer, CartListSerializer, OrderCreateSerializer
from apps.orders.models import Cart, Order


class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CartUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart
    serializer_class = CartSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CartCreate(generics.CreateAPIView):
    queryset = Cart
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderCreate(generics.CreateAPIView):
    queryset = Order
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)