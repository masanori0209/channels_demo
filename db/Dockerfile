FROM mysql:5.7

ADD ./init.sql /docker-entrypoint-initdb.d/init.sql
ADD ./my.cnf /etc/mysql/my.cnf
RUN chmod 644 /etc/mysql/my.cnf
