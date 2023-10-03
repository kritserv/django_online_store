## Developer Guide

#### command to grant privileges to the root user in MySQL or MariaDB:

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

#### command to fix Nginx Bad Gateway:

```
sudo netstat -nlp | grep 3306
sudo netstat -nlp | grep 8000
```

if the PID of that process was 12345, you would use `sudo kill 12345` to terminate that process.

```
sudo kill 12345
```