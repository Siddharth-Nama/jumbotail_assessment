#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed dummy data automatically into the Render ephemeral SQLite DB
python manage.py seed_data
