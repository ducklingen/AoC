.PHONY: lint test format install-pipx install-poetry install-project install

## Install scripts
install-pipx:
	pip install --upgrade pip
	python3 -m pip install --user pipx

install-poetry:
	pipx install poetry

install-project:
	poetry install

install: \
	install-pipx \
	install-poetry \
	install-project \


## Run tests
test: 
	poetry run pytest tests

## Lint code
lint:
	poetry run ruff check . --output-format concise

## Format python code
format:
	poetry run ruff format .

## Format python aggressively
format-aggressively: format
	poetry run ruff . --fix

## Type checking
type-check:
	poetry run pyright adventofcode