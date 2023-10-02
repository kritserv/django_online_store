from products.models import Smartphone
from math import floor

def GetAllSmartphoneData():

	filtered_smartphone =  Smartphone.objects.all()

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

	return smartphone_data