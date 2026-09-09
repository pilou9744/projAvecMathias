#!/bin/sh

PGDATA=/var/lib/postgresql/data

if [ ! -f $PGDATA ]
then
    initdb -d $PGDATA
fi

