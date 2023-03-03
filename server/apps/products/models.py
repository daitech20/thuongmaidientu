from django.db import models
from apps.users.models import User
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    keyword = models.ManyToManyField(Keyword, blank=True, related_name="categories_keyword")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products_brand")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products_category")
    keyword = models.ManyToManyField(Keyword, blank=True, related_name="products_keyword")

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments_product")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


from apps.orders.models import Order
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews_product")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="reviews_order")
    rate = models.IntegerField(default=5, blank=True)
    review = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images_user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images_product", null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="images_brand", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images_category", null=True, blank=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="images_review", null=True, blank=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)