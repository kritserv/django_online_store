## Online Ecommerce Shop example using Docker Django SQLite

preview: [ddice.pythonanywhere.com](https://ddice.pythonanywhere.com/)

<br>

some feature: 

- Filter product form
- Add to Cart, Remove from Cart
- Product summary
- Checkout form
- Login with Guest Account

<br>

### Installation

clone this repository:

```
git clone https://github.com/kritserv/django_online_store.git
```

- option 1: <a href="#virtualenv">Virtual Environment</a>
- option 2: <a href="#dockerengine">Docker Engine</a>


### virtualenv

Recommends **Python3.9**

```
cd django_online_store && cd app && pip install -r requirements.txt
```

> Run Server

```
python3 manage.py runserver
```

Open <a href="127.0.0.1:8000">127.0.0.1:8000/</a>

```
127.0.0.1:8000/
```

Runserver

### dockerengine

```
docker-compose up -d --build
```

## License:

[GNU General Public License v3.0](LICENSE)
