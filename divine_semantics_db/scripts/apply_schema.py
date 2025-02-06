import mysql.connector
import os
from dotenv import load_dotenv

import config

# Load environment variables
load_dotenv()

# Database connection
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

# Read schema file
with open(os.path.join(config.APP_DIR, "database/schema.sql"), "r") as f:
    schema_sql = f.read()

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Execute schema
    for statement in schema_sql.split(";"):
        if statement.strip():
            cursor.execute(statement)

    print("✅ Schema applied successfully!")

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
