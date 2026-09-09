FROM alpine:3.24.1

RUN apk add postgresql18 postgresql18-contrib

COPY init-postgres.sh /init-postgres.sh

USER postgres

CMD [ "/bin/sh", "/init-postgres.sh" ]