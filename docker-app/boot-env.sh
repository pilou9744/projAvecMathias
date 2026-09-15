#!/bin/sh

PGDATA=/var/lib/postgresql/data

if [ ! -s "$PGDATA/PG_VERSION" ]; then
    initdb -D "$PGDATA"
    echo "host all all 0.0.0.0/0 trust" >> "$PGDATA/pg_hba.conf"
    echo "listen_addresses = '*'" >> "$PGDATA/postgresql.conf"
fi

postgres -D "$PGDATA" &

until pg_isready -q; do
    sleep 1
done

psql --dbname=postgres --file=/schema.sql

cd /home/postgres/app/src

uvicorn main:app --host 0.0.0.0 --reload
