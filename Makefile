#!make
include .env
export $(shell sed 's/=.*//' .env)

start:
	@poetry run uvicorn app.main:app --host $(LOCAL_HOST) --port $(LOCAL_PORT) --reload
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

.PHONY: test autotype lint sa format start