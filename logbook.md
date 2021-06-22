# Implementation in python

# database: use POSTGIS in a docker container
* Accessed through well-known port 5432
```
docker run -d --name wd_pgis -e POSTGRES_PASSWORD=w@ste123 -e PGDATA=/var/lib/postgresql/data/pgdata --mount type=bind,source=c:/pgdata,target=/var/lib/postgresql/data -p 5432:5432 postgis/postgis
```
* Interact with **DBeaver**. Good overview here https://scottogletree.com/post/docker/

# API module

## Choice of framework:
* Django, supports REST API implementation and PostGIS extension, GeoDjango
https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/postgis/
On Windows, GeoDjango install through https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/#windows

* Will get datamodel and ORM from Django
* Good tutorial at https://dev.to/jkaylight/django-rest-framework-with-postgresql-a-crud-tutorial-1l34

### Installing Django, REST framework and postgre:
`pip install django djangorestframework psycopg2` (use the updated `requirements.txt`

## Generate django project
`django-admin startproject wd_project`

Update DB settings to point to our DB

## Generate Django App
`python manage.py startapp wd_api`, and add it to `INSTALLED_APPS`
