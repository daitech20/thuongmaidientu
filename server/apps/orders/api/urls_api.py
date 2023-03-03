from django.urls import include, path
from apps.orders.api.api_views import CartList, CartCreate, CartUpdate, OrderCreate


urlpatterns = [
    path('cart-list/', CartList.as_view()),
    path('cart-create/', CartCreate.as_view()),
    path('cart-update/<int:id>', CartUpdate.as_view()),
    path('order-create/', OrderCreate.as_view()),
]