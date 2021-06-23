docker run -d --name wd_gis --mount type=bind,source=c:/pgdata,target=/var/lib/postgresql/data -p 5432:5432 wd_postgis
