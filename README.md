<div style="text-align: right">
<img src="https://github.com/gmunumel/duck-simulator/actions/workflows/python-tests.yml/badge.svg"></img>
</div>

# duck-simulator

This project is to implement Duck Simulator follow Head First Pattern Chapter 12.

## Using virtual environment

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment:

In windows:

    . ./.venv/Scripts/activate

In linux:

    source .venv/bin/activate

## Install the libraries

    pip install .

or

    pip install .[test]

## Run the application

    python main.py

## Run the tests

    pytest -v

## Run Docker container

    docker build -t duck-simulator . && docker run --rm --name "duck-simulator" duck-simulator
