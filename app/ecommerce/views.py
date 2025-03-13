from .models import Product, Cart, CheckoutOrder, OrderProduct, Category, Brand, UserReview
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from guest_user.decorators import allow_guest_user
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import stripe
# This test secret API key is a placeholder. Don't include personal details in requests with this key.
# To see your test secret API key embedded in code samples, sign in to your Stripe account.
# You can also find your test secret API key at https://dashboard.stripe.com/test/apikeys.
stripe.api_key = 'sk_test_0QcpU1z0LTkqnbM2xwSgkV9500o3nNRTSO'
YOUR_DOMAIN = 'http://127.0.0.1:8000'

def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, "index.html", context={
        'categories': categories,
        'brands': brands,
        })

def product_list(request):
    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    products = []
    title = ''
    description = ''
    filter_option = []
    
    if category_id:
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category__id=category_id)
        
        filter_option = dict()
        for product in products:
            for field in product.category.filter_field.split(','):
                if getattr(product, field):
                    if filter_option.get(field):
                        filter_option[field].add(getattr(product, field))
                    else:
                        filter_option[field] = {getattr(product, field)}
        
        filter_conditions = []
        for key in request.GET.keys():
            if key != 'category' and key != 'page':
                values = request.GET.getlist(key)
                if values:
                    or_conditions = [f"{key}='{value}'" for value in values]
                    filter_conditions.append("(" + " OR ".join(or_conditions) + ")")
        
        if filter_conditions:
            where_clause = " AND ".join(filter_conditions)
            products = Product.objects.raw(f"SELECT * FROM ecommerce_product WHERE category_id={category_id} AND {where_clause}")
        
        title = category.name
        description = category.description
    
    if brand_id:
        products = Product.objects.filter(brand__id=brand_id)
        brand = Brand.objects.get(id=brand_id)
        title = brand.name
        description = brand.description
    
    # Pagination
    page = request.GET.get('page', 1)
    
    if isinstance(products, list) or hasattr(products, '__iter__'):
        products_list = list(products)
    else:
        products_list = list(products)
    
    paginator = Paginator(products_list, 5)
    
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)
    
    return render(request, "product_list.html", context={
        'products': products_page,
        'title': title,
        'description': description,
        'filter_option': filter_option,
        'category_id': category_id,
    })

@login_required
@allow_guest_user
def cart(request):
    cart = Cart.objects.filter(user__id=request.user.id, checkout=False).first()
    products = []
    total = 0
    if cart:
        products = cart.order_products.all()
        total = "{0:,.2f}".format(sum([product.product.current_price * product.quantity for product in products]))
    return render(request, "cart.html", context={
        'products': products,
        'total': total,
        })

@login_required
@allow_guest_user
def add_to_cart(request):
    product_id = request.GET.get('product')
    if not product_id:
        return redirect('cart')
    
    product = Product.objects.get(id=product_id)
    user = request.user
    
    cart, created = Cart.objects.get_or_create(
        user=user,
        checkout=False
    )
    
    existing_order = OrderProduct.objects.filter(
        user=user,
        product=product,
        cart__checkout=False
    ).first()
    
    if existing_order:
        existing_order.quantity += 1
        existing_order.save()
    else:
        order_product = OrderProduct.objects.create(
            user=user,
            product=product,
            quantity=1
        )
        cart.order_products.add(order_product)
    
    return redirect('cart')

@login_required
@allow_guest_user
def remove_from_cart(request):
    product_id = request.GET.get('product')
    if not product_id:
        return redirect('cart')
    
    order_product = OrderProduct.objects.get(
        id=product_id,
        user=request.user
    )
    cart = Cart.objects.get(user=request.user, checkout=False)
    
    if order_product.quantity > 1:
        order_product.quantity -= 1
        order_product.save()
    else:
        cart.order_products.remove(order_product)
        order_product.delete()
        
    return redirect('cart')

@login_required
@allow_guest_user
def checkout(request):
    PRICE_ID = 'a'
    try:
        session = stripe.checkout.Session.create(
            ui_mode = 'embedded',
            line_items=[
                {
                    'price': PRICE_ID,
                    'quantity': 1,
                },
            ],
            mode='payment',
            return_url=YOUR_DOMAIN + '/return?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        session = None
    return render(request, "checkout.html", context={

        })

@login_required
@allow_guest_user
def return_checkout(request):
    cart = Cart.objects.get(user=request.user, checkout=False)
    cart.checkout = True
    cart.save()
    products = cart.order_products.all()
    total = sum([product.product.current_price * product.quantity for product in products])
    
    shipping_address = request.POST.get('shipping_address')
    billing_address = request.POST.get('billing_address')
    
    checkout_order = CheckoutOrder.objects.create(
        user=request.user,
        cart=cart,
        state='progress',
        shipping_address=shipping_address,
        billing_address=billing_address,
        total_amount=total,
    )
    checkout_order.save()
    
    for product in products:
        product.product.available_quantity -= product.quantity
        product.product.save()
    
    return render(request, "return.html")


def product_detail(request):
    product_id = request.GET.get('product')
    if product_id:
        product = Product.objects.get(id=product_id)

    review_star = request.GET.get('star')
    review_comment = request.GET.get('comment', '')
    review_image = request.GET.get('image')

    if review_star and request.user:
        if request.user.username:
            product_review = UserReview.objects.create(
                image_link=review_image,
                user=request.user,
                comment=review_comment,
                star=review_star,
            )
            product.review.add(product_review)

    stars = '0.0'
    detail_fields = ((field, getattr(product, field)) for field in product.category.filter_field.split(','))
    if product.review.count():
        stars = "{0:,.2f}".format(sum([review.star for review in product.review.all()])/product.review.count())
    return render(request, "product_detail.html", context={
        'product': product,
        'detail_fields': detail_fields,
        'stars': stars,
        })

def check_account(request):
    user = request.user.username
    if user:
        return redirect(account_profile)
    else:
        return redirect('/login')

def register_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", context={
        'form': form
        })

def delete_account(request):
    user = request.user
    try:
        user.delete()
    except NotImplementedError:
        pass
    return redirect('/login')

@allow_guest_user
def login_guest(request):
    return redirect(account_profile)

def account_profile(request):
    user = request.user
    return render(request, "account_profile.html", context={
        'user': user
        })


def search_product(request):
    query = request.GET.get("q")
    if query:
        products = Product.objects.filter(name__icontains=query)
        return render(request, "product_list.html", context={
            "products": products,
            "title": f"Search result for: {query}",
            "description": '',
            })
    else:
        return redirect('home')