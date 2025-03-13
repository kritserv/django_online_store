from django.urls import path
from ecommerce.views import home, product_list, cart, \
	add_to_cart, remove_from_cart, checkout, return_checkout, search_product, product_detail, \
	check_account, login_guest, account_profile, register_account, delete_account

urlpatterns = [
	path('', home, name='home'),
	path('product_list', product_list, name='product_list'),
	path('cart', cart, name='cart'),
	path('add_to_cart', add_to_cart, name='add_to_cart'),
	path('remove_from_cart', remove_from_cart, name='remove_from_cart'),
	path('checkout', checkout, name='checkout'),
	path('return_checkout', return_checkout, name='return_checkout'),
	path('search_product', search_product, name='search_product'),
	path('product_detail', product_detail, name='product_detail'),
	path('check_account', check_account, name='check_account'),
	path('delete_account', delete_account, name='delete_account'),
    path('login_guest', login_guest, name='login_guest'),
    path('register_account', register_account, name='register_account'),
    path('accounts/profile/', account_profile, name='account_profile')
]