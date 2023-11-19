say-hello:
	echo "Hello World!"

docker-build:
	docker build -t="simple-server-image" .

docker-rerun:
	docker rm simple-server-container || true
	docker run --name=simple-server-container -p 8000:8000 simple-server-image

run-infra:
	docker-compose up postgres

install:
	pip3 install -r requirements.txt

run:
	cd app && python3 entrypoint.py
