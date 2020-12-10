all: build clean
clean:
	rm -rf Dockerfile
	rm -rf docker-compose.yml
copy-dotenv:
	cp -n env.example .env
copy-dockerfile:
	cp docker/* .
build: copy-dotenv copy-dockerfile
	docker-compose build
start:
	docker-compose -f docker/docker-compose.yml up -d
stop:
	docker-compose -f docker/docker-compose.yml down
restart: stop start
