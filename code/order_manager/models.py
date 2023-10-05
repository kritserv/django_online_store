from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ProductItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    og_price = models.IntegerField()
    price = models.IntegerField()
    is_on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OrderProductItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    prod_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.prod_item.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderProductItem)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


ADDRESS_CHOICES = (
    ("B", "Billing"),
    ("S", "Shipping"),
)


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Addresses"
