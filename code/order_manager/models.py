from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

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
    quantity = models.IntegerField(default=1)

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