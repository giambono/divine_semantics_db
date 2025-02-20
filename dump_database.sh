#!/bin/bash

# Extract DB_FILE from config.py
DB_FILE=$(python3 -c "import config; print(config.DB_FILE)")
if [ -z "$DB_FILE" ]; then
    echo "Error: DB_FILE not found in config.py"
    exit 1
fi

# Get the directory of DB_FILE
DB_DIR=$(dirname "$DB_FILE")

# Variables
SCHEMA_FILE="$DB_DIR/schema.sql"  # Output file for the schema
DUMP_FILE="$DB_DIR/dump.sql"      # Output file for the full dump
GIT_REPO_DIR="."                  # Directory of the Git repository (current directory by default)

# Step 1: Dump the schema
echo "Dumping schema to $SCHEMA_FILE..."
sqlite3 "$DB_FILE" .schema > "$SCHEMA_FILE"

# Step 2: Dump the full database (schema + data)
echo "Dumping full database to $DUMP_FILE..."
sqlite3 "$DB_FILE" .dump > "$DUMP_FILE"

# Step 4: Commit the changes to Git
echo "Committing changes to Git..."
cd "$GIT_REPO_DIR" || { echo "Failed to change directory to $GIT_REPO_DIR"; exit 1; }
git add "$SCHEMA_FILE" "$DUMP_FILE"
git commit -m "Update database schema and data dump"
git push origin main

echo "✅ Database dumped and changes committed to Git."