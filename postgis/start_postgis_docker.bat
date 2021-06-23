docker run -d --name wd_pgis -e POSTGRES_PASSWORD=w@ste123 -e PGDATA=/var/lib/postgresql/data/pgdata --mount type=bind,source=c:/pgdata,target=/var/lib/postgresql/data -p 5432:5432 postgis/postgis
