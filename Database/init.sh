#!/bin/bash

# Wait for the MySQL server to be ready
until mysql -h"$MYSQL_HOST" -u"root" -p"$MYSQL_ROOT_PASSWORD" -e "SELECT 1"; do
  echo "Waiting for MySQL server to be available..."
  sleep 2
done

# Check if the 'shoe_store' database exists
db_exists=$(mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'shoe_store';" | tail -n 1)

if [ "$db_exists" -eq 0 ]; then
  echo "Creating the 'shoe_store' database..."
  mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE shoe_store; USE shoe_store; source /docker-entrypoint-initdb.d/init.sql;"
else
  echo "Database 'shoe_store' already exists. No need to create."
fi
