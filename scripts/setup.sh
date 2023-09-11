#!/bin/bash

# Create a new virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install dependencies on setup
source install_dependencies.sh
