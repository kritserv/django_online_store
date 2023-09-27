from django.shortcuts import render
from django.views.generic.edit import FormView
from products.models import *
from .forms import ComputerForm

# Create your views here.
def home(request):
	return render(request, "homepage.html")

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
				filtered_computer = filtered_computer.filter(id__in=all_is_in_stock_query)
		query = None

		for query in form.cleaned_data['on_sale']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_on_sale=query).values_list('id'):
					all_is_on_sale_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_is_on_sale_query)
		query = None

		for query in form.cleaned_data['laptop']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_laptop=query).values_list('id'):
					all_is_laptop_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_is_laptop_query)
		query = None

		for query in form.cleaned_data['gaming']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(is_gamingtype=query).values_list('id'):
					all_gaming_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_gaming_query)
		query = None

		for query in form.cleaned_data['color']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(color=query).values_list('id'):
					all_color_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_color_query)
		query = None

		for query in form.cleaned_data['cpu']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(cpu=query).values_list('id'):
					all_cpu_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_cpu_query)
		query = None

		for query in form.cleaned_data['cpu_brand']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(cpu_brand=query).values_list('id'):
					all_cpu_brand_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_cpu_brand_query)
		query = None

		for query in form.cleaned_data['ram']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(ram=query).values_list('id'):
					all_ram_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_ram_query)
		query = None

		for query in form.cleaned_data['gpu']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(gpu=query).values_list('id'):
					all_gpu_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_gpu_query)
		query = None

		for query in form.cleaned_data['gpu_brand']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(gpu_brand=query).values_list('id'):
					all_qpu_brand_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_qpu_brand_query)
		query = None

		for query in form.cleaned_data['storage_size']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(storage=query).values_list('id'):
					all_storage_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_storage_query)
		query = None

		for query in form.cleaned_data['operating_system']:
			if query:
				at_least_1_query = True
				for x in filtered_computer.filter(os=query).values_list('id'):
					all_os_query.append(x[0])
				filtered_computer = filtered_computer.filter(id__in=all_os_query)

		if at_least_1_query == False:
			filtered_computer = Computer.objects.all()

		computer_id = [x[0] for x in filtered_computer.values_list('id')]
		computer_title = [x[0] for x in filtered_computer.values_list('title')]
		computer_img = filtered_computer.values_list('image')
		computer_img = [x[0].replace(' ','%20') for x in computer_img]
		computer_price = [str(x[0]) for x in filtered_computer.values_list('price')]
		computer_star = [str(x[0]) for x in filtered_computer.values_list('stars')]

		product_data = []
		for i in range(len(computer_title)):
			product_data.append({'id':computer_id[i], 'title':computer_title[i], 'im':computer_img[i], 'price':computer_price[i], 'star':computer_star[i]})

		self.request.session['product_data'] = product_data

		return super().form_valid(form)

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['product_data'] = self.request.session.get('product_data', [])
		return context