# Makefile for Python FastAPI project

# Set the default Python interpreter (can be overridden)
PYTHON = python3

# Virtual environment directory
VENV = venv

# Install project dependencies
all:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m venv $(VENV)
	source $(VENV)/bin/activate
	$(VENV)/bin/pip install -r requirements.txt