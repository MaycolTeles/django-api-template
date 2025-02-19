#!/bin/bash

# Script to setup the backend by:
# 1. Setting up a new poetry environment
# 2. Installing dependencies
# 3. Installing pre-commit hooks

poetry init

poetry lock

poetry install

poetry run pre-commit install
