PROJECT_PATH=./

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

pip:
	pip-compile --upgrade requirements/requirements.in --output-file  requirements/requirements.txt
	pip-compile --upgrade requirements/requirements-dev.in --output-file  requirements/requirements-dev.txt
	pip-sync requirements/requirements-dev.txt

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	flake8 --exclude=.tox,venv
