#!make
include .env
export $(shell sed 's/=.*//' .env)

start:
	@poetry run uvicorn app.main:app --host $(APP_HOST) --port $(APP_PORT) --reload
debug:
	@poetry run uvicorn app.main:app --host $(APP_HOST) --port $(APP_PORT) --log-config=log_config.yaml --reload
test:
	@poetry run pytest
autotype:
	@poetry run python -m libcst.tool codemod autotyping.AutotypeCommand app --aggressive
lint:
	@poetry run pylint app
sa:
	@poetry run mypy app
format:
	@poetry run black app
	@poetry run isort app

envcheck:
	env

.PHONY: test autotype lint sa format start debug