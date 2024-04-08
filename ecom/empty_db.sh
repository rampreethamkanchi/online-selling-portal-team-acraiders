#!/bin/bash

# Remove default database
rm db.sqlite3

# Remove migrations
rm -rf store/migrations

# Create new migrations
# python manage.py makemigrations ecom
python manage.py makemigrations store

# Apply migrations
python manage.py migrate