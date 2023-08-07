# Makefile for setting up a virtual environment and installing dependencies

all: venv activate upgrade-pip install-deps

# Create a virtual environment
venv:
	python -m venv venv

# Activate the virtual environment
activate:
	. venv/bin/activate

# Install or upgrade pip in the virtual environment
upgrade-pip: activate
	python -m pip install --upgrade pip

# Install dependencies from requirements.txt
install-deps: activate upgrade-pip
	pip install -r requirements.txt

# Phony targets to ensure these rules are always executed
.PHONY: all
