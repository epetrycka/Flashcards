# syntax=docker/dockerfile:1
FROM mysql:9.1.0
WORKDIR /.
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3306
CMD ["mysqld"]