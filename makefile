# Makefile
# Load environment variables from .env file
include .env
export

build:
	docker build -t mysql-image .

run:
	docker run -d -p $(DB_PORT):$(DB_PORT)/tcp --name $(CONTAINER_NAME) \
		-e MYSQL_ROOT_PASSWORD=$(DB_ROOT_PASSWORD) \
		-e MYSQL_DATABASE=$(DB_NAME) \
		-e MYSQL_USER=$(DB_USER) \
		-e MYSQL_PASSWORD=$(DB_PASSWORD) \
		mysql/mysql-server:latest

stop:
	docker stop $(CONTAINER_NAME)

remove:
	docker rm $(CONTAINER_NAME)

clean: stop remove

.PHONY: build run stop remove clean
