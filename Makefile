PYTHON ?= .venv/bin/python3.10

install:
	python3.10 -m venv .venv
	$(PYTHON) -m pip install "poetry==1.6.1"
	$(PYTHON) -m poetry install --no-root

lint:
	pre-commit run -a

jup:
	. .venv/bin/activate
	$(PYTHON) -m jupyterlab

jup-darwin:
	. .venv/bin/activate
	$(PYTHON) -m jupyterlab --app-dir=/opt/homebrew/share/jupyter/lab
