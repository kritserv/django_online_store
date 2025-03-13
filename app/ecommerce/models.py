from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    image = models.ImageField(upload_to='static/img/categories/', blank=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    filter_field = models.TextField(blank=True)
    detail_field = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    image = models.ImageField(upload_to='static/img/brands/', blank=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserReview(models.Model):
    image_link = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    star = models.FloatField(default=0.0, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.comment

class ProductCarousel(models.Model):
    image = models.ImageField(upload_to='static/img/products/', blank=True)

    def __str__(self):
        return self.image.url


class Product(models.Model):
    image = models.ImageField(upload_to='static/img/products/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    carousel = models.ManyToManyField(ProductCarousel, blank=True)
    name = models.CharField(max_length=200, blank=False)
    short_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=250, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)

    original_price = models.FloatField(default=100, blank=False)
    current_price = models.FloatField(default=100, blank=False)
    review = models.ManyToManyField(UserReview, blank=True)
    available_quantity = models.IntegerField(default=100, blank=False)

    theme = models.CharField(max_length=100, blank=True)
    cpu = models.CharField(max_length=100, blank=True)
    cpu_brand = models.CharField(max_length=20, blank=True)
    gpu = models.CharField(max_length=100, blank=True)
    gpu_brand = models.CharField(max_length=20, blank=True)
    ram = models.CharField(max_length=20, blank=True)
    bus = models.IntegerField(blank=True, null=True)
    storage = models.CharField(max_length=20, blank=True)
    storage_type = models.CharField(max_length=5, choices=(('hdd', 'HDD'), ('ssd', 'SSD')), blank=True)
    os = models.CharField(max_length=100, blank=True)
    resolution = models.CharField(max_length=20, blank=True)
    refresh_rate = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.short_name

    def format_original_price(self):
        return "{0:,.2f}".format(self.original_price)

    def format_current_price(self):
        return "{0:,.2f}".format(self.current_price)

    def discount_percentage(self):
        if self.original_price > 0:
            res = ((self.original_price - self.current_price) / self.original_price) * 100
            return "{0:,.2f}".format(res)
        return False

    def is_in_stock(self):
        return self.available_quantity > 0


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def total_price(self):
        return "{0:,.2f}".format(self.quantity * self.product.current_price)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_products = models.ManyToManyField(OrderProduct)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class CheckoutOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=(('progress', 'Progress'), ('confirm', 'Confirm'), ('delivery', 'Delivery'), ('done', 'Done')))
    shipping_address = models.TextField(blank=True)
    billing_address = models.TextField(blank=True)
    total_amount = models.FloatField(default=0.0, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username