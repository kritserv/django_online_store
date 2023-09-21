## Developer Guide

#### Command for give privileges to root

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
