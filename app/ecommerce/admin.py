from django.contrib import admin
from .models import Category, Brand, UserReview, ProductCarousel, Product, OrderProduct, Cart, CheckoutOrder
from django.utils.html import format_html

class AdminShowImage(admin.ModelAdmin):
	def show_image(self, obj):
		if obj.image:
			return format_html('<img src="{}" width="64" />'.format(obj.image.url))
		else:
			return "No image"

class CategoryAdmin(AdminShowImage):
	list_display = ["show_image", "name"]

admin.site.register(Category, CategoryAdmin)

class BrandAdmin(AdminShowImage):
	list_display = ["show_image", "name"]

admin.site.register(Brand, BrandAdmin)

class UserReviewAdmin(admin.ModelAdmin):
	list_display = ["user", "comment", "star"]

admin.site.register(UserReview, UserReviewAdmin)

class ProductCarouselAdmin(AdminShowImage):
	list_display = ["show_image", "image"]

admin.site.register(ProductCarousel, ProductCarouselAdmin)

class ProductAdmin(AdminShowImage):
	list_display = ["show_image", "name"]

admin.site.register(Product, ProductAdmin)

class OrderProductAdmin(AdminShowImage):
	list_display = ["user", "product", "quantity"]

admin.site.register(OrderProduct, OrderProductAdmin)

class CartAdmin(AdminShowImage):
	list_display = ["user", "checkout"]

admin.site.register(Cart, CartAdmin)

class CheckoutOrderAdmin(AdminShowImage):
	list_display = ["user", "state", "total_amount", "created_at", "updated_at"]

admin.site.register(CheckoutOrder, CheckoutOrderAdmin)