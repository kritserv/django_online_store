from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from products.models import *
from order_manager.models import *
from math import floor

# Create your views here.
def home(request):
    return render(request, "homepage.html")

def product_computer(request, id):
    product = Computer.objects.get(id=id)
    fullstar = "★" * floor(product.stars)
    return render(request, "store/product/computer.html", {'data': product, 'fullstar': fullstar})

@login_required
def add_to_cart(request, title):
    prod_item = get_object_or_404(ProductItem, title=title)
    order_item, created = OrderProductItem.objects.get_or_create(prod_item=prod_item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        
        if order.items.filter(prod_item=prod_item, ordered=False).exists():
            order_item = order.items.get(prod_item=prod_item, ordered=False)
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order_item = OrderProductItem.objects.create(prod_item=prod_item, user=request.user, ordered=False)
        order.items.add(order_item)

    return redirect("view_product_computer", id=Computer.objects.get(title=title).id)