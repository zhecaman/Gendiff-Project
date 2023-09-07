build:
	poetry build
lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report json
	
install:
	python3 -m pip install --user dist/*.whl