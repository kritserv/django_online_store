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

	def form_valid(self, form):

		filtered_computer = Computer.objects.all()

		self.request.session['computer_data'] = []

		for query in form.cleaned_data['product_available']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(is_in_stock=query)
				query = None

		for query in form.cleaned_data['on_sale']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(is_on_sale=query)
				query = None

		for query in form.cleaned_data['laptop']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(is_laptop=query)
				query = None

		for query in form.cleaned_data['gaming']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(is_gamingtype=query)
				query = None

		for query in form.cleaned_data['color']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(color=query)
				query = None

		for query in form.cleaned_data['cpu']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(cpu=query)
				query = None

		for query in form.cleaned_data['cpu_brand']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(cpu_brand=query)
				query = None

		for query in form.cleaned_data['ram']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(ram=query)
				query = None

		for query in form.cleaned_data['gpu']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(gpu=query)
				query = None

		for query in form.cleaned_data['gpu_brand']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(gpu_brand=query)
				query = None

		for query in form.cleaned_data['storage_size']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(storage=query)
				query = None

		for query in form.cleaned_data['operating_system']:
			print(query)
			if query:
				filtered_computer = filtered_computer.filter(os=query)
				query = None

		computer_id = [x[0] for x in filtered_computer.values_list('id')]

		computer_title = [x[0] for x in filtered_computer.values_list('title')]

		computer_img = filtered_computer.values_list('image')
		computer_img = [x[0].replace(' ','%20') for x in computer_img]

		computer_price = [str(x[0]) for x in filtered_computer.values_list('price')]

		computer_star = [str(x[0]) for x in filtered_computer.values_list('stars')]

		computer_data = []
		for i in range(len(computer_title)):
			computer_data.append({'id':computer_id[i], 'title':computer_title[i], 'im':computer_img[i], 'price':computer_price[i], 'star':computer_star[i]})

		self.request.session['computer_data'] = computer_data

		return super().form_valid(form)

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['computer_data'] = self.request.session.get('computer_data', [])
		return context