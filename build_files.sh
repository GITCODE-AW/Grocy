#!/bin/bash

# This script is for building static files

# Exit immediately if a command exits with a non-zero status
set -e

# Install Python dependencies
pip install -r requirments.txt

# Collect static files
python manage.py collectstatic --noinput
