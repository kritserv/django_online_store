from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from products.models import *
from order_manager.models import *
from math import floor

from .get_first_request.get_all_computer_data import GetAllComputerData
from .get_first_request.get_all_smartphone_data import GetAllSmartphoneData
from .get_first_request.get_all_headphone_data import GetAllHeadphoneData

# Create your views here.
def home(request):

	if 'computer_data' not in request.session:
		request.session['computer_data'] = GetAllComputerData()

	if 'smartphone_data' not in request.session:
		request.session['smartphone_data'] = GetAllSmartphoneData()

	if 'headphone_data' not in request.session:
		request.session['headphone_data'] = GetAllHeadphoneData()

	return render(request, "homepage.html")

def product_computer(request, id):
	product = Computer.objects.get(id=id)
	fullstar = "★" * floor(product.stars)
	return render(request, "store/product/computer.html", {'data': product, 'fullstar': fullstar})

def product_smartphone(request, id):
	product = Smartphone.objects.get(id=id)
	fullstar = "★" * floor(product.stars)
	return render(request, "store/product/smartphone.html", {'data': product, 'fullstar': fullstar})

def product_headphone(request, id):
	product = Headphone.objects.get(id=id)
	fullstar = "★" * floor(product.stars)
	return render(request, "store/product/headphone.html", {'data': product, 'fullstar': fullstar})

@login_required
def add_to_cart(request, title):
	prod_item = get_object_or_404(ProductItem, title=title)    
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	
	if order_qs.exists():
		order = order_qs[0]
		
		if order.items.filter(prod_item=prod_item, ordered=False).exists():
			order_item, created = order.items.get_or_create(prod_item=prod_item, ordered=False)
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item quality from your cart was updated.")
			return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
		else:
			order_item = OrderProductItem.objects.create(prod_item=prod_item, user=request.user, ordered=False)
			order.items.add(order_item)
			messages.info(request, "This item was added to your cart.")
			return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order_item = OrderProductItem.objects.create(prod_item=prod_item, user=request.user, ordered=False)
		order.items.add(order_item)
		messages.info(request, "This item was added to from your cart.")
		return redirect("view_product_computer", id=Computer.objects.get(title=title).id)

@login_required
def remove_from_cart(request, title):
	prod_item = get_object_or_404(ProductItem, title=title)
	order_qs = Order.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]

		if order.items.filter(prod_item__title=prod_item.title).exists():
			order_item = OrderProductItem.objects.filter(prod_item=prod_item, user=request.user, ordered=False)[0]
			order.items.remove(order_item)
			order_item.delete()
			messages.info(request, "This item was removed from your cart.")
			return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
		else:
			messages.info(request, "This item was not in your cart")
			return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
	else:
		messages.info(request, "You do not have an active order")
		return redirect("view_product_computer", id=Computer.objects.get(title=title).id)


@login_required
def remove_single_item_from_cart(request, title):
	prod_item = get_object_or_404(ProductItem, title=title)
	order_qs = Order.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]

		if order.items.filter(prod_item__title=prod_item.title).exists():
			order_item = OrderProductItem.objects.filter(prod_item=prod_item, user=request.user, ordered=False)[0]
			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
				messages.info(request, "This item quantity was updated.")
				return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
			else:
				order.items.remove(order_item)
				messages.info(request, "This item quantity was updated.")
				return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
		else:
			messages.info(request, "This item was not in your cart")
			return redirect("view_product_computer", id=Computer.objects.get(title=title).id)
	else:
		messages.info(request, "You do not have an active order")
		return redirect("view_product_computer", id=Computer.objects.get(title=title).id)