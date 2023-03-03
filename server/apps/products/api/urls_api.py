from django.urls import include, path
from apps.products.api.api_views import ProductCreate, ProductList, \
    CategoryList, BrandList, ProductUpdate, BrandCreate, CategoryCreate, \
    BrandUpdate, CategoryUpdate, ProductView



urlpatterns = [
    path('product-create/', ProductCreate.as_view()),
    path('product/update/<int:id>', ProductUpdate.as_view()),
    path('product/<int:id>', ProductView.as_view()),
    path('product-list/', ProductList.as_view()),
    path('category-list/', CategoryList.as_view()),
    path('brand-list/', BrandList.as_view()),
    path('brand/<int:id>', BrandUpdate.as_view()),
    path('category/<int:id>', CategoryUpdate.as_view()),
    path('category-create/', CategoryCreate.as_view()),
    path('brand-create/', BrandCreate.as_view()),
]