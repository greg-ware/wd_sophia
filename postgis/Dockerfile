# DockerFile to run postgis for WasteDrones project 
#
# Allow for some additional settings from base Docker Registry image
#
# Run with e.g. docker run -d --name wd_gis --mount type=bind,source=c:/pgdata,target=/var/lib/postgresql/data -p 5432:5432 wd_postgis

FROM postgis/postgis

RUN apt-get update && apt-get install -y procps

ENV POSTGRES_PASSWORD=w@ste123

ENV PGDATA=/var/lib/postgresql/data/pgdata

RUN echo using pasword $POSTGRES_PASSWORD

