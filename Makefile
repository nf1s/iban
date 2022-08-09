setup:
	@pipenv install --dev --pre

run:
	@pipenv run uvicorn main:app --reload

shell:
	@pipenv run python ipython

test:
	@pipenv run pytest

docker-build:
	@docker-compose build

docker-run:
	@docker-compose up

docker-shell:
	@docker-compose run web bash

docker-ipython:
	@docker-compose run web ipython

docker-test:
	@docker-compose run web pytest
