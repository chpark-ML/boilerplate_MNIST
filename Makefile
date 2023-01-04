SERVICE=core
COMMAND = /bin/zsh
PROJECT_NAME = "${SERVICE}-${USR}"
PROJECT_ROOT = /opt/core

build: 
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose -p ${PROJECT_NAME} up --build -d ${SERVICE}
up:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose -p ${PROJECT_NAME} up -d ${SERVICE}
exec:  
	DOCKER_BUILDKIT=1 docker compose -p ${PROJECT_NAME} exec ${SERVICE} ${COMMAND}
start:  
	docker compose -p ${PROJECT_NAME} start ${SERVICE}
down:  
	docker compose -p ${PROJECT_NAME} down
run: 
	docker compose -p ${PROJECT_NAME} run ${SERVICE} ${COMMAND}