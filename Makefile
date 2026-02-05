.PHONY: help install lint format test pre-commit migrate makemigrations run docker-up docker-down

help:
	@echo "Targets: install | lint | format | test | pre-commit | makemigrations | migrate | run | docker-up | docker-down"

install:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt

lint:
	ruff check .
	isort --check-only .
	black --check .

format:
	isort .
	black .
	ruff check . --fix

test:
	pytest

pre-commit:
	pre-commit run --all-files

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down