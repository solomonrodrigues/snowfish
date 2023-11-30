#!/bin/bash

# Set the log file path
#LOG_FILE="$(dirname "${BASH_SOURCE[0]}")/build.log"

# Redirect all output to the log file
#exec > >(tee -i "$LOG_FILE")
#exec 2>&1

# Print a timestamp to the log
#echo "Build started: $(date)"

# Install dependencies
pip install -r requirements.txt

python3.9 manage.py collectstatic

# Make migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate

python3.9 manage.py createsuperuser --noinput

# Print a timestamp to the log
#echo "Build completed: $(date)"
