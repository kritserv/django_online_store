from django.contrib import admin
from .models import Brand, Computer, Smartphone

# Register your models here.
admin.site.register(Brand)
admin.site.register(Computer)
admin.site.register(Smartphone)