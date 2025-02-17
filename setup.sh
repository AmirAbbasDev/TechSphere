#!/bin/bash

# Create a Python virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv env

# Activate the virtual environment
echo "Activating the virtual environment..."
source env/bin/activate

# Install project dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r ./requirements/requirements.txt

# Install project dependencies from requirements.txt
echo "Installing tailwindcss dependencies..."
cd theme/static_src
npm install
cd ../../

# Make database migrations
# echo "Making database migrations..."
# python3 manage.py makemigrations

# Apply database migrations
echo "Applying database migrations..."
python3 manage.py migrate

# Run the Django development server
echo "Starting the Django development server on port 5600..."
python3 manage.py runserver 5600
