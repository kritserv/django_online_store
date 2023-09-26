from django.shortcuts import render
from django.views.generic.edit import FormView
from products.models import *
from .forms import ComputerForm

# Create your views here.
def home(request):
	return render(request, "homepage.html")

class ComputerFormView(FormView):

	form_class = ComputerForm
	template_name = 'products/computer.html'
	success_url = '/computer'