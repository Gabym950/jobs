.PHONY: help install lint format test pre-commit docker-up docker-down run

help:
	@echo "Targets: install | lint | format | test | pre-commit | docker-up | docker-down | run"

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

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down

run:
	python3 -m app.main