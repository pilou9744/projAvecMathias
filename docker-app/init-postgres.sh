#!/bin/sh

PGDATA=/var/lib/postgresql/data

if [ ! -s "$PGDATA/PG_VERSION" ]; then
    initdb -D "$PGDATA"
fi

exec postgres -D "$PGDATA"

