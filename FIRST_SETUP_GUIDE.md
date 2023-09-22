# First time setup guide



## Insert data to database via python shell

Shell into python app from code-app-1 terminal

```
python manage.py shell
```

Import product models

```
from products.models import *
```

Adding data

```
Brand(id=1, title="Zeus", image="media/model_img/brands/Zues.png").save()

Computer(id=1, title="Zeus Olymus ZOTO-a5-010", brand=Brand.objects.get(title="Zeus"), image="media/model_img/computers/pctest.jpg", color="White", is_in_stock = True, in_stocks = 10, is_on_sale = True, og_price = 45000, price = 39000, stars = 4.9, is_recommend = True, is_laptop = False, is_gamingtype = True, has_monitor = False, cpu = "Reda a5-6500", cpu_brand = "Reda", ram = "16Gb", gpu = "RD 6700", gpu_brand = "Reda", storage = "1Tb", storage_type = "Ssd", size = None, case = "Atx", resolution = None, refresh_rate = None, display = None, weight = 5.67, os = "Windows11").save()

```
