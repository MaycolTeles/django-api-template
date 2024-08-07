.PHONY: setup
setup:
	./scripts/setup.sh


.PHONY: run
run:
	cd app && poetry run python manage.py runserver 0.0.0.0:8000


.PHONY: run-prod
run-prod:
	cd app && poetry run gunicorn core.wsgi --bind 0.0.0.0:8000


.PHONY: migrations
migrations:
	poetry run python app/manage.py makemigrations


.PHONY: migrate
migrate:
	poetry run python app/manage.py migrate


.PHONY: shell
shell:
	poetry run python app/manage.py shell


.PHONY: test
test:
	poetry run pytest app/ -v -n auto


.PHONY: coverage
coverage:
	poetry run pytest app/ -v -n auto --html=test_report/test-report.html --cov-report=html


.PHONY: lint
lint:
	poetry run ruff check


.PHONY: format
format:
	poetry run ruff format


.PHONY: format-check
format-check:
	poetry run ruff format --check


.PHONY: install-dev
install-dev:
	poetry install --with dev


.PHONY: install-prod
install-prod:
	poetry install --with prod


.PHONY: commit
commit: poetry run pre-commit run --all-files


# Remove build artifacts
.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


# Remove Python file artifacts
.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


# Remove test and coverage artifacts
.PHONY: clean-test
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr test_report/


# Remove all build, test, coverage and Python artifacts
.PHONY: clean
clean: clean-build clean-pyc clean-test
