#!/bin/sh

PGDATA=/var/lib/postgresql/data

if [ ! -f $PGDATA ]
then
    initdb -d $PGDATA
fi

export PATH="$PATH:/home/postgres/go/bin"

flog -f rfc3164 -l -d 3s