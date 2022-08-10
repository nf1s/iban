setup:
	@pipenv install --dev --pre

run:
	@pipenv run uvicorn main:app --reload

shell:
	@pipenv run python ipython

unit-test:
	@pipenv run pytest tests/unit --cov app/ --no-cov-on-fail --cov-report term-missing

integration-test:
	@pipenv run pytest tests/integration --cov api/ --no-cov-on-fail --cov-report term-missing

lint:
	@pipenv run flake8
	@pipenv run mypy .

test: lint unit-test integration-test

docker-build:
	@docker-compose build

docker-run:
	@docker-compose up --build

docker-shell:
	@docker-compose run web bash

docker-ipython:
	@docker-compose run web ipython

docker-test:
	@docker-compose run web pytest

deploy:
	@skaffold run

delete:
	@skaffold delete
