from django.shortcuts import render
from django.views.generic.edit import FormView
from products.models import *
from .forms import ComputerForm
from math import floor

# Create your views here.
def home(request):
	return render(request, "homepage.html")

def product_computer(request, id):
	product = Computer.objects.get(id=id)
	return render(request, "store/product/computer.html", {'data': product})

class ComputerFormView(FormView):

	form_class = ComputerForm
	template_name = 'store/product.html'
	success_url = '/computer'

	def form_valid(self, form):

		filtered_computer =  Computer.objects.all()

		self.request.session['product_data'] = []
		all_is_in_stock_query, all_is_on_sale_query, all_is_laptop_query, all_gaming_query, all_color_query, all_cpu_query, all_cpu_brand_query, all_ram_query, all_gpu_query, all_qpu_brand_query, all_storage_query, all_os_query = [], [], [], [], [], [], [], [], [], [], [], []
		at_least_1_query = False

		for query in form.cleaned_data['product_available']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_in_stock=query).values_list('id'):
					all_is_in_stock_query.append(x[0])
		if form.cleaned_data['product_available']:
			filtered_computer = filtered_computer.filter(id__in=all_is_in_stock_query)
		query = None

		for query in form.cleaned_data['on_sale']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_on_sale=query).values_list('id'):
					all_is_on_sale_query.append(x[0])
		if form.cleaned_data['on_sale']:	
			filtered_computer = filtered_computer.filter(id__in=all_is_on_sale_query)
		query = None

		for query in form.cleaned_data['laptop']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_laptop=query).values_list('id'):
					all_is_laptop_query.append(x[0])
		if form.cleaned_data['laptop']:	
			filtered_computer = filtered_computer.filter(id__in=all_is_laptop_query)
		query = None

		for query in form.cleaned_data['gaming']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_gamingtype=query).values_list('id'):
					all_gaming_query.append(x[0])
		if form.cleaned_data['gaming']:	
			filtered_computer = filtered_computer.filter(id__in=all_gaming_query)
		query = None

		for query in form.cleaned_data['color']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(color=query).values_list('id'):
					all_color_query.append(x[0])
		if form.cleaned_data['color']:
			filtered_computer = filtered_computer.filter(id__in=all_color_query)
		query = None

		for query in form.cleaned_data['cpu']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(cpu=query).values_list('id'):
					all_cpu_query.append(x[0])
		if form.cleaned_data['cpu']:
			filtered_computer = filtered_computer.filter(id__in=all_cpu_query)
		query = None

		for query in form.cleaned_data['cpu_brand']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(cpu_brand=query).values_list('id'):
					all_cpu_brand_query.append(x[0])
		if form.cleaned_data['cpu_brand']:
			filtered_computer = filtered_computer.filter(id__in=all_cpu_brand_query)
		query = None

		for query in form.cleaned_data['ram']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(ram=query).values_list('id'):
					all_ram_query.append(x[0])
		if form.cleaned_data['ram']:
			filtered_computer = filtered_computer.filter(id__in=all_ram_query)
		query = None

		for query in form.cleaned_data['gpu']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(gpu=query).values_list('id'):
					all_gpu_query.append(x[0])
		if form.cleaned_data['gpu']:
			filtered_computer = filtered_computer.filter(id__in=all_gpu_query)
		query = None

		for query in form.cleaned_data['gpu_brand']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(gpu_brand=query).values_list('id'):
					all_qpu_brand_query.append(x[0])
		if form.cleaned_data['gpu_brand']:
			filtered_computer = filtered_computer.filter(id__in=all_qpu_brand_query)
		query = None

		for query in form.cleaned_data['storage_size']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(storage=query).values_list('id'):
					all_storage_query.append(x[0])
		if form.cleaned_data['storage_size']:
			filtered_computer = filtered_computer.filter(id__in=all_storage_query)
		query = None

		for query in form.cleaned_data['operating_system']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(os=query).values_list('id'):
					all_os_query.append(x[0])
		if form.cleaned_data['operating_system']:
			filtered_computer = filtered_computer.filter(id__in=all_os_query)

		if at_least_1_query == False:
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

		self.request.session['product_data'] = product_data

		return super().form_valid(form)

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['product_data'] = self.request.session.get('product_data', [])
		return context