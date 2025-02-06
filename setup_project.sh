#!/bin/bash

# Define project name
PROJECT_NAME="divine_comedy_db"

# Create the main project directory
mkdir -p $PROJECT_NAME/{database,data,scripts,docs}

# Create database-related files
touch $PROJECT_NAME/database/{schema.sql,seed_data.sql,insert_data.sql,queries.sql,migrate.sql}

# Create data folder for CSV files
touch $PROJECT_NAME/data/{dante_original.csv,translations.csv,commentaries.csv}

# Create Python script for loading data
touch $PROJECT_NAME/scripts/load_csv.py

# Create documentation
touch $PROJECT_NAME/docs/README.md

# Initialize a Git repository
cd $PROJECT_NAME
git init
echo "Project structure created successfully!"
