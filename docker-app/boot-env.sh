#!/bin/sh

PGDATA=/var/lib/postgresql/data

if [ ! -s "$PGDATA/PG_VERSION" ]; then
    initdb -D "$PGDATA"
fi

postgres -D "$PGDATA" &

until pg_isready -q; do
    sleep 1
done

psql --dbname=postgres --file=/schema.sql

cd /home/postgres/app

uvicorn src.main:app --host 0.0.0.0 --reload &
cd /home/postgres/app/src_flog

python3 flog_to_api.py

# flog -f rfc3164 -l -d 2
