from rest_framework import permissions
from rest_framework import generics, status
from apps.products.api.serializers import ProductCreateSerializer, ProductListSerializer, CategorySerializer, BrandSerializer
from apps.products.models import Product, Category, Brand


class ProductCreate(generics.CreateAPIView):
    queryset = Product
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductList(generics.ListAPIView):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductListSerializer


class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = 'id'


class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandCreate(generics.CreateAPIView):
    queryset = Brand
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class CategoryCreate(generics.CreateAPIView):
    queryset = Category
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'