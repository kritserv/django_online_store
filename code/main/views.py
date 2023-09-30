from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from products.models import *
from order_manager.models import *
from math import floor

# Create your views here.
def home(request):

    if 'product_data' not in request.session:
        filtered_computer = Computer.objects.all()

        computer_title = [x[0] for x in filtered_computer.values_list('title')]
        computer_link = ['/computer/product/'+str(x[0]) for x in filtered_computer.values_list('id')]
        computer_onsale = [x[0] for x in filtered_computer.values_list('is_on_sale')]
        computer_og_price = [x[0] for x in filtered_computer.values_list('og_price')]
        computer_price = [x[0] for x in filtered_computer.values_list('price')]
        computer_is_in_stock = [x[0] for x in filtered_computer.values_list('is_in_stock')]
        computer_in_stocks = [x[0] for x in filtered_computer.values_list('in_stocks')]
        computer_is_recommend  = [x[0] for x in filtered_computer.values_list('is_recommend')]
        computer_img = filtered_computer.values_list('image')
        computer_img = [x[0].replace(' ','%20') for x in computer_img]
        computer_price = [str(x[0]) for x in filtered_computer.values_list('price')]
        computer_star = [str(x[0]) for x in filtered_computer.values_list('stars')]

        product_data = []
        for i in range(len(computer_title)):

            if computer_onsale[i] == False:
                computer_og_price[i] = ''
            fullstar = "★" * floor(float(computer_star[i]))

            if computer_onsale[i] == True:
                computer_onsale[i] = 'Sale'
            else:
                computer_onsale[i] = ''

            if computer_is_in_stock[i] == False:
                computer_is_in_stock[i] = 'Out of Stock'
            else:
                computer_is_in_stock[i] = 'In Stocks'

            if computer_is_recommend[i] == True:
                computer_is_recommend[i] = 'Recommend'
            else:
                computer_is_recommend[i] = ''

            if len(computer_title[i] + 'Recommend') > 37:
                computer_title[i] = computer_title[i][0:30] + '...'


            product_data.append({'title':computer_title[i], 'onsale':computer_onsale[i], 
                'ogprice':computer_og_price[i], 'price':computer_price[i],'im':computer_img[i], 
                'instock':computer_is_in_stock[i], 'available': computer_in_stocks[i], 'link': computer_link[i],
                'recommend':computer_is_recommend[i], 'star':fullstar, 'star_num':' ('+computer_star[i]+')'})

        request.session['product_data'] = product_data

    return render(request, "homepage.html")

def product_computer(request, id):
    product = Computer.objects.get(id=id)
    fullstar = "★" * floor(product.stars)
    return render(request, "store/product/computer.html", {'data': product, 'fullstar': fullstar})

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