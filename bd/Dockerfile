FROM mysql:latest

ENV MYSQL_USER=lepoxa
ENV MYSQL_ROOT_PASSWORD=lepoxa

EXPOSE 3306

COPY init.sql /docker-entrypoint-initdb.d/

CMD ["mysqld"]
