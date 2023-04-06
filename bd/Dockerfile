FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_USER=lepoxa
ENV MYSQL_PASSWORD=lepoxa

ADD ./bd/init.sql /docker-entrypoint-initdb.d

EXPOSE 3306/tcp
