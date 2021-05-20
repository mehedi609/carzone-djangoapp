## Necessary Commands

**_install virtual env:_**
1. `pip install virtualenv`
2. `python -m venv venv`


**_activate the virtualenv_**
1. `venv\Scripts\activate.bat`

_**install the django**_
1. `pip install django==3.0.7`

_**create a django project**_
1. django-admin startproject carzone .

_**create new app**_
1. `python manage.py startapp app-name`\
ex. `python manage.py startapp pages`

_**install postgresql database driver**_
1. `pip install psycopg2`

_**postgresql database**_
1. if you don't have postgresql you can download it from here [postgresql](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
2. Please install version 12.*
3. create a database named _**carzone_db**_
4. You can watch this [video](https://www.youtube.com/watch?v=AEZg-sTxxmw) to install postgresql

_**migration commands**_
1. `python manage.py makemigrations`
2. `python manage.py migrate`
    * this commands should be run from root dir

_**create superuser**_
1. `python manage.py createsuperuser`
* give username, email, and password. you can bypass the security if you want