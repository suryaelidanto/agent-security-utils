.PHONY: setup dev test lint up down

# Install all dependencies including dev-groups
setup:
	uv sync
	uv run pre-commit install

# Run the local development server with auto-reload
dev:
	uv sync
	uv run pre-commit install
	uv run uvicorn app.main:app --reload --port 8000

# Run all tests using pytest
test:
	uv run pytest

# Fix linting and format code using ruff
lint:
	uv run ruff check . --fix
	uv run ruff format .

# Build and start the containerized service
up:
	docker compose up --build

# Stop and remove containers
down:
	docker compose down
