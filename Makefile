clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

pip:
	pip-compile requirements/requirements.in --output-file --update requirements/requirements.txt
	pip-compile requirements/requirements-dev.in --output-file --update requirements/requirements-dev.txt

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
