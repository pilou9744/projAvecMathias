FROM alpine:3.24.1

RUN apk add postgresql18 postgresql18-contrib

RUN install -d -o postgres -g postgres /run/postgresql

COPY init-postgres.sh /init-postgres.sh

# Accepte le script aussi bien avec des fins de ligne Windows (CRLF) que Linux (LF).
RUN sed -i 's/\r$//' /init-postgres.sh

USER postgres

CMD [ "/bin/sh", "/init-postgres.sh" ]
