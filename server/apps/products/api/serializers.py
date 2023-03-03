from rest_framework import serializers
from apps.users.models import User
from apps.products.models import Product, Category, Brand
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from drf_extra_fields.fields import Base64ImageField


class ProductCreateSerializer(serializers.ModelSerializer):   
    image = Base64ImageField(required=False) 
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        
        if user.is_superuser:
            return super().create(validated_data)
        else:
            raise serializers.ValidationError({"user": "k co quyen"})


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'