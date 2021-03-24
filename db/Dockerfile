FROM mysql:5

ENV MYSQL_ROOT_PASSWORD 123
ENV MYSQL_DATABASE discounts
ENV MYSQL_USER discount_service
ENV MYSQL_PASSWORD 123
ADD create-discount-db.sql /docker-entrypoint-initdb.d
