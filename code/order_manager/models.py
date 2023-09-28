from django.db import models
from django.conf import settings 

# Create your models here.

class ProductItem(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField()
	og_price = models.IntegerField()
	price = models.IntegerField()

	def __str__(self):
		return self.title

class OrderProductItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	prod_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username