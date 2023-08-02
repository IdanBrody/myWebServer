FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=Kuku1234!
ENV MYSQL_DATABASE=shoe_store
# ENV MYSQL_USER=root
# ENV MYSQL_PASSWORD=Kuku1234!

COPY init.sql /docker-entrypoint-initdb.d/
COPY init.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init.sh

