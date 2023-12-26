# alembic-bugreport
## To reproduce
```shell
docker compose up -d
mkdir alembic/versions
alembic revision --autogenerate  # creates 1st migration
alembic upgrade head
alembic revision --autogenerate  # creates 2nd migration, even though nothing was changed
```

