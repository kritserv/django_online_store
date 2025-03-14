## Online Ecommerce Shop example using Django SQLite


https://github.com/user-attachments/assets/7e9353f3-2284-4862-8f53-9b67ed3ff742


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
- option 2: <a href="#dockerengine">Docker</a>


### virtualenv

Recommends **Python3.9+**

```
cd app && pip install -r requirements.txt
```

> **Migrate** and **Load** dump data

```
python3 manage.py migrate
```

```
python3 manage.py loaddata dumped_data.json
```

> Run Server

```
python3 manage.py runserver
```

```
127.0.0.1:8000/
```

### dockerengine

```
docker-compose up -d --build
```

```
127.0.0.1:8000/
```

## License:

[GNU General Public License v3.0](LICENSE)
