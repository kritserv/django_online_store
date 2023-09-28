from django.shortcuts import render
from products.models import *
from math import floor

# Create your views here.
def home(request):
	return render(request, "homepage.html")

def product_computer(request, id):
	product = Computer.objects.get(id=id)
	fullstar = "★" * floor(product.stars)
	return render(request, "store/product/computer.html", {'data': product, 'fullstar': fullstar})