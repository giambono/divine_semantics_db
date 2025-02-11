#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define project root directory
PROJECT_DIR="$HOME/IdeaProjects/divine_semantics_db"

# Activate virtual environment
source "$PROJECT_DIR/venv/bin/activate"

# Set PYTHONPATH
export PYTHONPATH="$PROJECT_DIR"

# Create the database
echo "🚀 Creating database..."
python "$PROJECT_DIR/divine_comedy_db/scripts/create_db.py"

# Apply schema
echo "📜 Applying schema..."
python "$PROJECT_DIR/divine_comedy_db/scripts/apply_schema.py"

# Load data: Original Dante Text
echo "📥 Loading Dante original text..."
python "$PROJECT_DIR/divine_comedy_db/scripts/load_data_dante_original.py"

# Load data: Translations
echo "📥 Loading translations..."
python "$PROJECT_DIR/divine_comedy_db/scripts/load_data_translations.py"

# Load data: Outlines
echo "📥 Loading outlines..."
python "$PROJECT_DIR/divine_comedy_db/scripts/load_data_outlines.py"

echo "✅ Database replication completed successfully!"
