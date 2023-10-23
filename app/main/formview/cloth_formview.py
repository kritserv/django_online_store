from django.shortcuts import render
from django.views.generic.edit import FormView
from products.models import Cloth
from main.form.cloth_form import ClothForm
from math import floor


class ClothFormView(FormView):
    form_class = ClothForm
    template_name = "store/product.html"
    success_url = "/cloth"

    def form_valid(self, form):
        filtered_cloth = Cloth.objects.all()

        self.request.session["cloth_data"] = []
        (
            all_is_in_stock_query,
            all_is_on_sale_query,
            all_color_query,
            all_gender_query,
            all_cloth_type_query,
            all_size_query,
        ) = ([], [], [], [], [], [])
        at_least_1_query = False

        for query in form.cleaned_data["product_available"]:
            if query:
                at_least_1_query = True
                for x in filtered_cloth.filter(is_in_stock=query).values_list("id"):
                    all_is_in_stock_query.append(x[0])
        if form.cleaned_data["product_available"]:
            filtered_cloth = filtered_cloth.filter(id__in=all_is_in_stock_query)
        query = None

        for query in form.cleaned_data["on_sale"]:
            if query:
                at_least_1_query = True
                for x in filtered_cloth.filter(is_on_sale=query).values_list("id"):
                    all_is_on_sale_query.append(x[0])
        if form.cleaned_data["on_sale"]:
            filtered_cloth = filtered_cloth.filter(id__in=all_is_on_sale_query)
        query = None

        for query in form.cleaned_data["color"]:
            if query:
                at_least_1_query = True
                for x in filtered_cloth.filter(color=query).values_list("id"):
                    all_color_query.append(x[0])
        if form.cleaned_data["color"]:
            filtered_cloth = filtered_cloth.filter(id__in=all_color_query)
        query = None

        for query in form.cleaned_data["gender"]:
            if query:
                at_least_1_query = True
                for x in filtered_cloth.filter(gender=query).values_list("id"):
                    all_gender_query.append(x[0])
        if form.cleaned_data["gender"]:
            filtered_cloth = filtered_cloth.filter(id__in=all_gender_query)
        query = None

        for query in form.cleaned_data["cloth_type"]:
            if query:
                at_least_1_query = True
                for x in filtered_cloth.filter(cloth_type=query).values_list("id"):
                    all_cloth_type_query.append(x[0])
        if form.cleaned_data["cloth_type"]:
            filtered_cloth = filtered_cloth.filter(id__in=all_cloth_type_query)
        query = None

        for query in form.cleaned_data["size"]:
            if query:
                at_least_1_query = True
                for x in filtered_cloth.filter(size=query).values_list("id"):
                    all_size_query.append(x[0])
        if form.cleaned_data["size"]:
            filtered_cloth = filtered_cloth.filter(id__in=all_size_query)
        query = None

        if at_least_1_query == False:
            filtered_cloth = Cloth.objects.all()

        cloth_title = [x[0] for x in filtered_cloth.values_list("title")]
        cloth_link = [
            "/cloth/product/" + str(x[0]) for x in filtered_cloth.values_list("id")
        ]
        cloth_onsale = [x[0] for x in filtered_cloth.values_list("is_on_sale")]
        cloth_og_price = [x[0] for x in filtered_cloth.values_list("og_price")]
        cloth_price = [x[0] for x in filtered_cloth.values_list("price")]
        cloth_is_in_stock = [x[0] for x in filtered_cloth.values_list("is_in_stock")]
        cloth_in_stocks = [x[0] for x in filtered_cloth.values_list("in_stocks")]
        cloth_is_recommend = [x[0] for x in filtered_cloth.values_list("is_recommend")]
        cloth_img = filtered_cloth.values_list("image")
        cloth_img = [x[0].replace(" ", "%20") for x in cloth_img]
        cloth_price = [str(x[0]) for x in filtered_cloth.values_list("price")]
        cloth_star = [str(x[0]) for x in filtered_cloth.values_list("stars")]

        cloth_data = []
        for i in range(len(cloth_title)):
            if cloth_onsale[i] == False:
                cloth_og_price[i] = ""
            fullstar = "★" * floor(float(cloth_star[i]))

            if cloth_onsale[i] == True:
                cloth_onsale[i] = "Sale"
            else:
                cloth_onsale[i] = ""

            if cloth_is_in_stock[i] == False:
                cloth_is_in_stock[i] = "Out of Stock"
            else:
                cloth_is_in_stock[i] = "In Stocks"

            if cloth_is_recommend[i] == True:
                cloth_is_recommend[i] = "Recommend"
            else:
                cloth_is_recommend[i] = ""

            if len(cloth_title[i] + "Recommend") > 37:
                cloth_title[i] = cloth_title[i][0:30] + "..."

            cloth_data.append(
                {
                    "title": cloth_title[i],
                    "onsale": cloth_onsale[i],
                    "ogprice": cloth_og_price[i],
                    "price": cloth_price[i],
                    "im": cloth_img[i],
                    "instock": cloth_is_in_stock[i],
                    "available": cloth_in_stocks[i],
                    "link": cloth_link[i],
                    "recommend": cloth_is_recommend[i],
                    "star": fullstar,
                    "star_num": " (" + cloth_star[i] + ")",
                }
            )

        self.request.session["cloth_data"] = cloth_data

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_data"] = self.request.session.get("cloth_data", [])
        return context