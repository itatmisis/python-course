docker-build:
	docker build -t="app" .

docker-rerun:
	docker rm app || true
	docker run --name=app -p 8000:8000 -e APP_UVICORN='{"host": "0.0.0.0"}' app

run-infra:
	docker-compose up postgres

install:
	pip3 install -r requirements.txt

run:
	cd app && python3 entrypoint.py
