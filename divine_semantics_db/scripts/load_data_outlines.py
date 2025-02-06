import mysql.connector
import os
import pandas as pd
from dotenv import load_dotenv
from pandas.io.formats.excel import ExcelCell

import config

from divine_semantics_db.scripts.utils import get_or_create_id

# Load environment variables
load_dotenv()

# Database connection configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

# Mapping cantica names to IDs
CANTICA_MAP = {"Inferno": 1, "Purgatorio": 2, "Paradiso": 3}

# Load CSV
EXCEL_FILE = os.path.join(config.APP_DIR, "data/outlines.xlsx")  # Adjust if needed
df = pd.read_excel(EXCEL_FILE)

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Insert translations into the database
    for _, row in df.iterrows():
        cantica_id = CANTICA_MAP.get(row["cantica"], None)
        if cantica_id is None:
            print(f"Skipping unknown cantica: {row['cantica']}")
            continue

        canto = int(row["canto"])
        start_verse = int(row["start_verse"])
        end_verse = int(row["end_verse"])

        author_id = get_or_create_id(cursor, "author", "name", row["author"])
        type_id = get_or_create_id(cursor, "type", "name", row["type"])

        text = row["text"]
        if text:
            cursor.execute(
                """INSERT INTO divine_comedy 
                (cantica_id, canto, start_verse, end_verse, text, author_id, type_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (cantica_id, canto, start_verse, end_verse, text, author_id, type_id),
            )

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ CSV data successfully imported!")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
