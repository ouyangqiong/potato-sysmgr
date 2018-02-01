# potato-sysmgr
## create database
```
CREATE DATABASE IF NOT EXISTS potato DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
## create tables
```
python manage.py migrate
python manage.py migrate sysmgr
```

