
## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-adminlte.git
$ cd django-adminlte
```

<br />

> 👉 Install modules via `VENV`  

Create .env file in root directory and copy-paste this or just run `cp env_sample .env`, :

```
DEBUG=True
SECRET_KEY=gix%#3&%giwv8f0+%r946en7z&d@9*rc$sl0qoq7z&d@9*rc$sl0qoql56xr%bh^w2mj
CSRF_TRUSTED_ORIGINS=http://192.168.1.66:5085
DJANGO_SUPERUSER_PASSWORD=demo

APPMSW_PARAM_NANE=Basic
APPMSW_LOGO_TITLE=MsW-Title
APPMSW_LOGO_FOOTER=MsW-Footer

# Connection string for iris
APPMSW_IRIS_URL=iris://superuser:SYS@iris:1972/USER
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
