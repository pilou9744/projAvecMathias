FROM alpine:3.24.1

RUN apk add postgresql18 postgresql18-contrib go py3-fastapi uvicorn

# RUN go install github.com/mingrammer/flog@latest
RUN go install github.com/mingrammer/flog@latest \
    && install -m 755 "$(go env GOPATH)/bin/flog" /usr/local/bin/flog

RUN install -d -o postgres -g postgres /run/postgresql

COPY boot-env.sh /boot-env.sh
COPY shema.sql /schema.sql

COPY ./src /home/postgres/app/src

COPY ./src_flog /home/postgres/app/src_flog

# Accepte le script aussi bien avec des fins de ligne Windows (CRLF) que Linux (LF).
RUN sed -i 's/\r$//' /boot-env.sh

USER postgres

CMD [ "/bin/sh", "/boot-env.sh" ]
