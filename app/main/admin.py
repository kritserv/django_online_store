from django.contrib import admin
from products.models import *
from order_manager.models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Computer)
admin.site.register(Smartphone)
admin.site.register(Headphone)
admin.site.register(Cloth)

admin.site.register(ProductItem)
admin.site.register(OrderProductItem)
admin.site.register(Order)