build:
	poetry build
install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report lcov
	
package-install:
	python3 -m pip install --user dist/*.whl
