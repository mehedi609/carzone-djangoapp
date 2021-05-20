## Necessary Commands

**_create virtual env:_** \
`python -m venv venv`

**_activate the virtualenv_** \
`venv\Scripts\activate.bat`

_**create a django project**_ \
`django-admin startproject carzone .`

_**create new app**_
* `python manage.py startapp app-name`\
ex. `python manage.py startapp pages`

_**postgresql database**_
1. if you don't have postgresql you can download it from here [postgresql](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
2. Please install version 12.*
3. create a database named _**carzone_db**_
4. You can watch this [video](https://www.youtube.com/watch?v=AEZg-sTxxmw) to install postgresql

_**migration commands**_
- `python manage.py makemigrations`
- `python manage.py migrate`
    * this commands should be run from root dir

_**create superuser**_
- `python manage.py createsuperuser`
   * give username, email, and password. you can bypass the security if you want

<br></br>

## Required Packages

**_install virtual env:_** \
`pip install virtualenv`

_**install the django**_ \
`pip install django==3.0.7`

_**install postgresql database driver**_ \
`pip install psycopg2`

_**install django-ckeditor package**_ \
`pip install django-ckeditor`\
have to include it in INSTALLED_APPS in settings file as 'ckeditor'

_**install Pillow package for image**_ \
`pip install Pillow`

_**install django-multiselectfield package**_ \
`pip install django-multiselectfield`