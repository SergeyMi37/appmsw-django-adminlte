[![Repo-GitHub](https://img.shields.io/badge/dynamic/xml?color=gold&label=GitHub%20module.xml&prefix=ver.&query=%2F%2FVersion&url=https%3A%2F%2Fraw.githubusercontent.com%2Fsergeymi37%2Fappmsw-django-adminlte%2Fmaster%2Fmodule.xml)](https://raw.githubusercontent.com/sergeymi37/appmsw-django-adminlte/master/module.xml)
[![OEX-zapm](https://img.shields.io/badge/dynamic/json?url=https:%2F%2Fpm.community.intersystems.com%2Fpackages%2Fappmsw-django-adminlte%2F&label=ZPM-pm.community.intersystems.com&query=$.version&color=green&prefix=appmsw-django-adminlte)](https://pm.community.intersystems.com/packages/appmsw-django-adminlte)

[![Docker-ports](https://img.shields.io/badge/dynamic/yaml?color=blue&label=docker-compose&prefix=ports%20-%20&query=%24.services.iris.ports&url=https%3A%2F%2Fraw.githubusercontent.com%2Fsergeymi37%2Fappmsw-django-adminlte%2Fmaster%2Fdocker-compose.yml)](https://raw.githubusercontent.com/sergeymi37/appmsw-django-adminlte/master/docker-compose.yml)

## appmsw-django-adminlte

![](https://raw.githubusercontent.com/SergeyMi37/appmsw-django-adminlte/master/doc/icons/AdminLTELogo.png)

Application tools for use Django AdminLte.

[![OEX](https://img.shields.io/badge/Available%20on-Intersystems%20Open%20Exchange-00b2a9.svg)](https://openexchange.intersystems.com/package/appmsw-django-adminlte) 
[![Demo](https://img.shields.io/badge/Demo%20on-Cloud%20Run%20Deploy-F4A460)](https://appmsw-django-adminlte.demo.community.intersystems.com/apptoolsrest/a/info)

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/SergeyMi37/appmsw-django-adminlte">

[![license](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://raw.githubusercontent.com/sergeymi37/appmsw-django-adminlte/master/LICENSE)

## What's new

Implemented support for connecting to IRIS via the JDBC library.

![](https://raw.githubusercontent.com/SergeyMi37/appmsw-django-adminlte/master/doc/icons/logo-apptools.png)

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/SergeyMi37/appmsw-django-adminlte.git
$ cd appmsw-django-adminlte
```

<br />

> 👉 Install modules via `VENV`  

Create .env file in root directory and copy-paste this or just run `cp env_sample .env`, :

```
DEBUG=True
SECRET_KEY=gix%#3&%giwv8f0+%r946en7z&d@9*rc$sl0qoq7z&d@9*rc$sl0qoql56xr%bh^w2mj
CSRF_TRUSTED_ORIGINS=http://real-you-IP:5085
DJANGO_SUPERUSER_PASSWORD=demo

APPMSW_PARAM_NANE=Basic
APPMSW_LOGO_TITLE=MsW-Title
APPMSW_LOGO_FOOTER=MsW-Footer

# Connection string for iris via Nativ Python libs
#APPMSW_IRIS_URL=iris://superuser:SYS@iris:1972/USER

# Connection string for iris via JDBC libs
APPMSW_IRIS_URL=jdbc://superuser:SYS@iris:1972/USER
```


```
python -m venv env
source env/bin/activate
source env/Scripts/activate # for Windows
pip install -r requirements.txt

pip install appmsw/api/intersystems_irispython-3.2.0-py3-none-any.whl
python -m pip install --upgrade pip
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # adm, developer
python manage.py loaddata db-init-param.json
python manage.py runserver

At this point, the app runs at `http://127.0.0.1:8000/`. 
