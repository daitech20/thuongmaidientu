from django.urls import include, path

app_name = "api"

users_urlpatterns = [
    path("users/", include("apps.users.api.urls_api")),
]

profiles_urlpatterns = [
    path("profiles/", include("apps.profiles.api.urls_api")),
]

orders_urlpatterns = [
     path("orders/", include("apps.orders.api.urls_api")),
]

products_urlpatterns = [
     path("products/", include("apps.products.api.urls_api")),
]

urlpatterns = [
    *users_urlpatterns,
    *profiles_urlpatterns,
    *orders_urlpatterns,
    *products_urlpatterns,
]