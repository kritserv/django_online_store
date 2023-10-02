from django.shortcuts import render
from django.views.generic.edit import FormView
from products.models import Headphone
from main.form.headphone_form import HeadphoneForm
from math import floor

class HeadphoneFormView(FormView):

    form_class = HeadphoneForm
    template_name = 'store/product.html'
    success_url = '/headphone'

    def form_valid(self, form):

        filtered_headphone =  Headphone.objects.all()

        self.request.session['headphone_data'] = []
        all_is_in_stock_query, all_is_on_sale_query, all_is_bluetooth_query, all_is_waterproof_query, all_has_noise_cancelling_query, all_has_microphone_query, all_color_query, all_headphone_type_query, all_port_query, all_frequency_response_query = [], [], [], [], [], [], [], [], [], []
        at_least_1_query = False

        for query in form.cleaned_data['product_available']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(is_in_stock=query).values_list('id'):
                    all_is_in_stock_query.append(x[0])
        if form.cleaned_data['product_available']:
            filtered_headphone = filtered_headphone.filter(id__in=all_is_in_stock_query)
        query = None

        for query in form.cleaned_data['on_sale']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(is_on_sale=query).values_list('id'):
                    all_is_on_sale_query.append(x[0])
        if form.cleaned_data['on_sale']:    
            filtered_headphone = filtered_headphone.filter(id__in=all_is_on_sale_query)
        query = None

        for query in form.cleaned_data['is_bluetooth']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(is_is_bluetooth=query).values_list('id'):
                    all_is_is_bluetooth_query.append(x[0])
        if form.cleaned_data['is_bluetooth']: 
            filtered_headphone = filtered_headphone.filter(id__in=all_is_is_bluetooth_query)
        query = None

        for query in form.cleaned_data['is_waterproof']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(is_waterproof=query).values_list('id'):
                    all_is_waterproof_query.append(x[0])
        if form.cleaned_data['is_waterproof']: 
            filtered_headphone = filtered_headphone.filter(id__in=all_is_waterproof_query)
        query = None

        for query in form.cleaned_data['has_noise_cancelling']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(has_noise_cancelling=query).values_list('id'):
                    all_has_noise_cancelling_query.append(x[0])
        if form.cleaned_data['has_noise_cancelling']: 
            filtered_headphone = filtered_headphone.filter(id__in=all_has_noise_cancelling_query)
        query = None
        
        for query in form.cleaned_data['has_microphone']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(has_microphone=query).values_list('id'):
                    all_has_microphone_query.append(x[0])
        if form.cleaned_data['has_microphone']: 
            filtered_headphone = filtered_headphone.filter(id__in=all_has_microphone_query)
        query = None

        for query in form.cleaned_data['color']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(color=query).values_list('id'):
                    all_color_query.append(x[0])
        if form.cleaned_data['color']:
            filtered_headphone = filtered_headphone.filter(id__in=all_color_query)
        query = None

        for query in form.cleaned_data['headphone_type']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(headphone_type=query).values_list('id'):
                    all_headphone_type_query.append(x[0])
        if form.cleaned_data['headphone_type']:
            filtered_headphone = filtered_headphone.filter(id__in=all_headphone_type_query)
        query = None

        for query in form.cleaned_data['port']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(port=query).values_list('id'):
                    all_port_query.append(x[0])
        if form.cleaned_data['port']:
            filtered_headphone = filtered_headphone.filter(id__in=all_port_query)
        query = None

        for query in form.cleaned_data['frequency_response']:
            if query:
                at_least_1_query = True
                for x in filtered_headphone.filter(frequency_response=query).values_list('id'):
                    all_frequency_response_query.append(x[0])
        if form.cleaned_data['frequency_response']:
            filtered_headphone = filtered_headphone.filter(id__in=all_frequency_response_query)
        query = None

        if at_least_1_query == False:
            filtered_headphone = Headphone.objects.all()

        headphone_title = [x[0] for x in filtered_headphone.values_list('title')]
        headphone_link = ['/headphone/product/'+str(x[0]) for x in filtered_headphone.values_list('id')]
        headphone_onsale = [x[0] for x in filtered_headphone.values_list('is_on_sale')]
        headphone_og_price = [x[0] for x in filtered_headphone.values_list('og_price')]
        headphone_price = [x[0] for x in filtered_headphone.values_list('price')]
        headphone_is_in_stock = [x[0] for x in filtered_headphone.values_list('is_in_stock')]
        headphone_in_stocks = [x[0] for x in filtered_headphone.values_list('in_stocks')]
        headphone_is_recommend  = [x[0] for x in filtered_headphone.values_list('is_recommend')]
        headphone_img = filtered_headphone.values_list('image')
        headphone_img = [x[0].replace(' ','%20') for x in headphone_img]
        headphone_price = [str(x[0]) for x in filtered_headphone.values_list('price')]
        headphone_star = [str(x[0]) for x in filtered_headphone.values_list('stars')]

        headphone_data = []
        for i in range(len(headphone_title)):

            if headphone_onsale[i] == False:
                headphone_og_price[i] = ''
            fullstar = "★" * floor(float(headphone_star[i]))

            if headphone_onsale[i] == True:
                headphone_onsale[i] = 'Sale'
            else:
                headphone_onsale[i] = ''

            if headphone_is_in_stock[i] == False:
                headphone_is_in_stock[i] = 'Out of Stock'
            else:
                headphone_is_in_stock[i] = 'In Stocks'

            if headphone_is_recommend[i] == True:
                headphone_is_recommend[i] = 'Recommend'
            else:
                headphone_is_recommend[i] = ''

            if len(headphone_title[i] + 'Recommend') > 37:
                headphone_title[i] = headphone_title[i][0:30] + '...'


            headphone_data.append({'title':headphone_title[i], 'onsale':headphone_onsale[i], 
                'ogprice':headphone_og_price[i], 'price':headphone_price[i],'im':headphone_img[i], 
                'instock':headphone_is_in_stock[i], 'available': headphone_in_stocks[i], 'link': headphone_link[i],
                'recommend':headphone_is_recommend[i], 'star':fullstar, 'star_num':' ('+headphone_star[i]+')'})

        self.request.session['headphone_data'] = headphone_data

        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['product_data'] = self.request.session.get('headphone_data', [])
        return context