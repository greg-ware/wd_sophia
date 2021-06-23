# Implementation in python

# database: use POSTGIS in a docker container
* Accessed through well-known port 5432
```
docker run -d --name wd_pgis -e POSTGRES_PASSWORD=w@ste123 -e PGDATA=/var/lib/postgresql/data/pgdata --mount type=bind,source=c:/pgdata,target=/var/lib/postgresql/data -p 5432:5432 postgis/postgis
```
* Interact with **DBeaver**. Good overview here https://scottogletree.com/post/docker/

# REST API module

## Choice of framework:
* Django, supports REST API implementation and PostGIS extension, GeoDjango
* Django has built-in scalability features

* Implementation will get datamodel and ORM to POstGIS from Django

### Implementation notes:
* https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/postgis/
* Intro at https://dev.to/jkaylight/django-rest-framework-with-postgresql-a-crud-tutorial-1l34
* On Windows, GeoDjango install through https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/#windows

### Installing Django, REST framework and postgre:
`pip install django djangorestframework psycopg2` (use the updated `requirements.txt`

## Outline
### Generate Django project
`django-admin startproject wd_project`

Update DB settings to point to our DB

### Generate Django App
`python manage.py startapp wd_api`, and add it to `INSTALLED_APPS`

-> Create data model, then expose REST endpoints

TODOs:
  1. Add GeoJSON support to Django: complete GeoDJango config
  2. Enhance model with more functional APIs, to be used by backend system

# Backend Service

The second component is a backend service responsible for gathering waste reports, dispatching the drones as necessary when the number of uncleaned waster for a given zone goes above the given threshold, and updating the computed per zone statistics (number of drone cleanups, number of reports, ...). As such it must simulate drone clean ups.

## Assumptions

### Drones control
Drones are interacting with backend OTA, using Kafka as communication bus
> Note: probably need MQTT rather than Kafka for the OTA part.

> **Note**: We need another Model for Drones, keeping a digital twin in the PostGIS DB

* Drone model:
  * **Drone**: Static drone information, plus possibly dynamic usage stats
  * **Flights**: Historian of drone flights
  * Possibly **Mission**  managed by the

* Need to define drone comms protocol, i.e. services rendered:
  * Backend-> drone:
     * Dispatch to Zone to clean-up waste
  * Drone-> backend:
     * Report position. Backend keeps track of drones whereabouts
     * Report waste cleanup success/failure

### Work Manager: Drone Missions
The backend service implementing business logic:
1. Background scheduled task to monitor new Waste Reports
  * Decision logic to create and monitor drone **Mission**s
2. Consumer for Drone operations (**Missions**)
  * Keep track of drone missions (**Flight** track)
3. Scheduled task for Drone Health check, verify that drones are still alive
4. ... probably many other functional requirements

## Kafka: Docker test env
There are several Kafka containerized solutions, most of them running with at least two containers (Kafka + ZooKeeper)

For prototyping testing purposes, find self-contained Kafka Broker (incl. ZooKeeper)
To do: check out https://github.com/spotify/docker-kafka

### DronesFleet: Drones simulator
In addition to the backend service, we will need a simulation of Drones Fleet
