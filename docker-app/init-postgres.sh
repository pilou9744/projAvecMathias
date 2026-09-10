#!/bin/sh

PGDATA=/var/lib/postgresql/data

if [ ! -s "$PGDATA/PG_VERSION" ]; then
    initdb -D "$PGDATA"
fi

# exec postgres -D "$PGDATA"
exec postgres -D "$PGDATA"

# export PATH="$PATH:/home/postgres/go/bin"

# flog -f rfc3164 -l -d 3s