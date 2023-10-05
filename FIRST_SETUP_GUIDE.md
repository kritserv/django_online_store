# First time setup guide

Change the directory to `/code`.

```
docker-compose up -d --build
```

# Important Step (Program Will Not Run Properly If Skipped!)

## After Docker Build Command

Stop the container; it will keep restarting because the database doesn't exist yet. Docker will not run migrations before Django runs successfully for the first time.

Insert hashtag to ignore following lines in the ddice_online_shop/urls.py:

```
...
20    #from main.formview.computer_formview import ComputerFormView
21    #from main.formview.smartphone_formview import SmartphoneFormView
22    #from main.formview.headphone_formview import HeadphoneFormView
23    #from main.formview.cloth_formview import ClothFormView

...

37        #path('computer/', ComputerFormView.as_view(), name='view_computer'),
38        #path('smartphone/', SmartphoneFormView.as_view(), name='view_smartphone'),
39        #path('headphone/', HeadphoneFormView.as_view(), name='view_headphone'),
40        #path('cloth/', ClothFormView.as_view(), name='view_cloth'),
...
```

Start docker-compose again. Then, remove these hashtags after migrations are completed. After that, restart the code-app image and proceed to the next step.

## Insert data to database via Python

Access the manage.py command from the code-app terminal:

```
python manage.py loaddata dumped_data.json
```
> restore dumped data from dumped_data.json

<br>

**Done!** Your first-time setup is now completed.

<br>
<br>

#### Other useful command:

- [grant privileges to the root in mysql](#command-to-grant-privileges-to-the-root-user-in-mysql-or-mariadb)

- [fix Nginx Bad Gateway](#command-to-fix-nginx-bad-gateway)

##### command to grant privileges to the root user in MySQL or MariaDB:

```
mysql -u root -p ddice_online_shop_database
```

```
ddice
```
> Password: ddice (same as settings.py)

```
GRANT ALL PRIVILEGES ON ddice_online_shop_database.* TO root@'%';
SHOW GRANTS FOR 'root';
```

##### command to fix Nginx Bad Gateway:

```
sudo netstat -nlp | grep 8000
```

if the PID of that process was 12345, you would use `sudo kill 12345` to terminate that process.

```
sudo kill 12345
```