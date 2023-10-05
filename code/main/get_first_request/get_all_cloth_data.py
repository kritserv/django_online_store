from products.models import Cloth
from math import floor


def GetAllClothData():
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

    return cloth_data
