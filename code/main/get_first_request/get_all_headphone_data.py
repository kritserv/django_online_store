from products.models import Headphone
from math import floor


def GetAllHeadphoneData():
    filtered_headphone = Headphone.objects.all()

    headphone_title = [x[0] for x in filtered_headphone.values_list("title")]
    headphone_link = [
        "/headphone/product/" + str(x[0]) for x in filtered_headphone.values_list("id")
    ]
    headphone_onsale = [x[0] for x in filtered_headphone.values_list("is_on_sale")]
    headphone_og_price = [x[0] for x in filtered_headphone.values_list("og_price")]
    headphone_price = [x[0] for x in filtered_headphone.values_list("price")]
    headphone_is_in_stock = [
        x[0] for x in filtered_headphone.values_list("is_in_stock")
    ]
    headphone_in_stocks = [x[0] for x in filtered_headphone.values_list("in_stocks")]
    headphone_is_recommend = [
        x[0] for x in filtered_headphone.values_list("is_recommend")
    ]
    headphone_img = filtered_headphone.values_list("image")
    headphone_img = [x[0].replace(" ", "%20") for x in headphone_img]
    headphone_price = [str(x[0]) for x in filtered_headphone.values_list("price")]
    headphone_star = [str(x[0]) for x in filtered_headphone.values_list("stars")]

    headphone_data = []
    for i in range(len(headphone_title)):
        if headphone_onsale[i] == False:
            headphone_og_price[i] = ""
        fullstar = "★" * floor(float(headphone_star[i]))

        if headphone_onsale[i] == True:
            headphone_onsale[i] = "Sale"
        else:
            headphone_onsale[i] = ""

        if headphone_is_in_stock[i] == False:
            headphone_is_in_stock[i] = "Out of Stock"
        else:
            headphone_is_in_stock[i] = "In Stocks"

        if headphone_is_recommend[i] == True:
            headphone_is_recommend[i] = "Recommend"
        else:
            headphone_is_recommend[i] = ""

        if len(headphone_title[i] + "Recommend") > 37:
            headphone_title[i] = headphone_title[i][0:30] + "..."

        headphone_data.append(
            {
                "title": headphone_title[i],
                "onsale": headphone_onsale[i],
                "ogprice": headphone_og_price[i],
                "price": headphone_price[i],
                "im": headphone_img[i],
                "instock": headphone_is_in_stock[i],
                "available": headphone_in_stocks[i],
                "link": headphone_link[i],
                "recommend": headphone_is_recommend[i],
                "star": fullstar,
                "star_num": " (" + headphone_star[i] + ")",
            }
        )

    return headphone_data
