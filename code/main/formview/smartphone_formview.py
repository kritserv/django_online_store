from django.shortcuts import render
from django.views.generic.edit import FormView
from products.models import Smartphone
from main.form.smartphone_form import SmartphoneForm
from math import floor

class SmartphoneFormView(FormView):

    form_class = SmartphoneForm
    template_name = 'store/product.html'
    success_url = '/smartphone'

    def form_valid(self, form):

        filtered_smartphone =  Smartphone.objects.all()

        self.request.session['smartphone_data'] = []
        all_is_in_stock_query, all_is_on_sale_query, all_is_tablet_query, all_flagship_query, all_color_query, all_processor_query, all_processor_brand_query, all_ram_query, all_storage_query, all_os_query, all_front_camera_query, all_back_camera_query, all_sim_query = [], [], [], [], [], [], [], [], [], [], [], [], []
        at_least_1_query = False

        for query in form.cleaned_data['product_available']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(is_in_stock=query).values_list('id'):
                    all_is_in_stock_query.append(x[0])
        if form.cleaned_data['product_available']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_is_in_stock_query)
        query = None

        for query in form.cleaned_data['on_sale']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(is_on_sale=query).values_list('id'):
                    all_is_on_sale_query.append(x[0])
        if form.cleaned_data['on_sale']:    
            filtered_smartphone = filtered_smartphone.filter(id__in=all_is_on_sale_query)
        query = None

        for query in form.cleaned_data['tablet']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(is_tablet=query).values_list('id'):
                    all_is_tablet_query.append(x[0])
        if form.cleaned_data['tablet']: 
            filtered_smartphone = filtered_smartphone.filter(id__in=all_is_tablet_query)
        query = None

        for query in form.cleaned_data['flagship']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(is_flagship=query).values_list('id'):
                    all_flagship_query.append(x[0])
        if form.cleaned_data['flagship']: 
            filtered_smartphone = filtered_smartphone.filter(id__in=all_flagship_query)
        query = None

        for query in form.cleaned_data['color']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(color=query).values_list('id'):
                    all_color_query.append(x[0])
        if form.cleaned_data['color']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_color_query)
        query = None

        for query in form.cleaned_data['processor']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(processor=query).values_list('id'):
                    all_processor_query.append(x[0])
        if form.cleaned_data['processor']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_processor_query)
        query = None

        for query in form.cleaned_data['processor_brand']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(processor_brand=query).values_list('id'):
                    all_processor_brand_query.append(x[0])
        if form.cleaned_data['processor_brand']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_processor_brand_query)
        query = None

        for query in form.cleaned_data['ram']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(ram=query).values_list('id'):
                    all_ram_query.append(x[0])
        if form.cleaned_data['ram']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_ram_query)
        query = None

        for query in form.cleaned_data['storage_size']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(storage=query).values_list('id'):
                    all_storage_query.append(x[0])
        if form.cleaned_data['storage_size']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_storage_query)
        query = None

        for query in form.cleaned_data['operating_system']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(os=query).values_list('id'):
                    all_os_query.append(x[0])
        if form.cleaned_data['operating_system']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_os_query)

        for query in form.cleaned_data['front_camera']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(front_camera=query).values_list('id'):
                    all_front_camera_query.append(x[0])
        if form.cleaned_data['front_camera']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_front_camera_query)

        for query in form.cleaned_data['back_camera']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(back_camera=query).values_list('id'):
                    all_back_camera_query.append(x[0])
        if form.cleaned_data['back_camera']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_back_camera_query)

        for query in form.cleaned_data['sim']:
            if query:
                at_least_1_query = True
                for x in filtered_smartphone.filter(sim=query).values_list('id'):
                    all_sim_query.append(x[0])
        if form.cleaned_data['sim']:
            filtered_smartphone = filtered_smartphone.filter(id__in=all_sim_query)

        if at_least_1_query == False:
            filtered_smartphone = Smartphone.objects.all()

        smartphone_title = [x[0] for x in filtered_smartphone.values_list('title')]
        smartphone_link = ['/smartphone/product/'+str(x[0]) for x in filtered_smartphone.values_list('id')]
        smartphone_onsale = [x[0] for x in filtered_smartphone.values_list('is_on_sale')]
        smartphone_og_price = [x[0] for x in filtered_smartphone.values_list('og_price')]
        smartphone_price = [x[0] for x in filtered_smartphone.values_list('price')]
        smartphone_is_in_stock = [x[0] for x in filtered_smartphone.values_list('is_in_stock')]
        smartphone_in_stocks = [x[0] for x in filtered_smartphone.values_list('in_stocks')]
        smartphone_is_recommend  = [x[0] for x in filtered_smartphone.values_list('is_recommend')]
        smartphone_img = filtered_smartphone.values_list('image')
        smartphone_img = [x[0].replace(' ','%20') for x in smartphone_img]
        smartphone_price = [str(x[0]) for x in filtered_smartphone.values_list('price')]
        smartphone_star = [str(x[0]) for x in filtered_smartphone.values_list('stars')]

        smartphone_data = []
        for i in range(len(smartphone_title)):

            if smartphone_onsale[i] == False:
                smartphone_og_price[i] = ''
            fullstar = "★" * floor(float(smartphone_star[i]))

            if smartphone_onsale[i] == True:
                smartphone_onsale[i] = 'Sale'
            else:
                smartphone_onsale[i] = ''

            if smartphone_is_in_stock[i] == False:
                smartphone_is_in_stock[i] = 'Out of Stock'
            else:
                smartphone_is_in_stock[i] = 'In Stocks'

            if smartphone_is_recommend[i] == True:
                smartphone_is_recommend[i] = 'Recommend'
            else:
                smartphone_is_recommend[i] = ''

            if len(smartphone_title[i] + 'Recommend') > 37:
                smartphone_title[i] = smartphone_title[i][0:30] + '...'


            smartphone_data.append({'title':smartphone_title[i], 'onsale':smartphone_onsale[i], 
                'ogprice':smartphone_og_price[i], 'price':smartphone_price[i],'im':smartphone_img[i], 
                'instock':smartphone_is_in_stock[i], 'available': smartphone_in_stocks[i], 'link': smartphone_link[i],
                'recommend':smartphone_is_recommend[i], 'star':fullstar, 'star_num':' ('+smartphone_star[i]+')'})

        self.request.session['smartphone_data'] = smartphone_data

        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['product_data'] = self.request.session.get('smartphone_data', [])
        return context