from products.models import Computer
from math import floor

def GetAllComputerData():

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
	computer_data = []

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


		computer_data.append({'title':computer_title[i], 'onsale':computer_onsale[i], 
			'ogprice':computer_og_price[i], 'price':computer_price[i],'im':computer_img[i], 
			'instock':computer_is_in_stock[i], 'available': computer_in_stocks[i], 'link': computer_link[i],
			'recommend':computer_is_recommend[i], 'star':fullstar, 'star_num':' ('+computer_star[i]+')'})

	return computer_data