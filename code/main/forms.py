from django import forms
from products.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ComputerForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Submit'))

	QUERY_FIELDS = ['is_in_stock', 'is_on_sale','is_laptop', 'is_gamingtype', 'cpu', 'cpu_brand', 'ram', 'gpu', 'gpu_brand', 'storage', 'os']

	FORM = []

	i = 0
	for q in QUERY_FIELDS:

		i+=1
		CHOICES = []
		for x in Computer.objects.values(q).distinct().order_by(q):
			CHOICES.append((x[q], x[q]))

		FORM.append(forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES, required=False))

	product_available = FORM[0]
	on_sale = FORM[1]
	laptop = FORM[2]
	gaming = FORM[3]
	cpu = FORM[4]
	cpu_brand = FORM[5]
	ram = FORM[6]
	gpu = FORM[7]
	gpu_brand = FORM[8]
	storage_size = FORM[9]
	operating_system = FORM[10]