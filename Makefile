.PHONY: setup dev test lint up down

setup:
	uv sync

dev:
	uv sync
	uv run uvicorn app.main:app --reload --port 8000

test:
	uv run pytest

lint:
	uv run ruff check . --fix
	uv run ruff format .

up:
	docker compose up --build

down:
	docker compose down
