# How to run sedafw cli on docker

## Prerequisites

### Install make
    sudo apt install make

### Install docker-ce
https://docs.docker.com/install/linux/docker-ce/ubuntu/

### Install docker-compose
https://docs.docker.com/compose/install/

## How to use
Build docker image and make default .env file with make

    make

Open .env file with your favorite editor and set environment variables

    DI_EXAMPLE_MYSQL_HOST=MYSQL_HOST_PLACEHOLDER
    DI_EXAMPLE_MYSQL_PORT=3306
    DI_EXAMPLE_MYSQL_DATABASE=MYSQL_DATABAES_PLACEHOLDER
    DI_EXAMPLE_MYSQL_USERNAME=MYSQL_USERNAME_PLACEHOLDER
    DI_EXAMPLE_MYSQL_PASSWORD=MYSQL_PASSWORD_PLACEHOLDER
    ...
    ...

Run a docker container

    make start

Execute script with container

    docker exec -ti docker_codegrok-indexer_1 python3 -m di.module showCurrentTime