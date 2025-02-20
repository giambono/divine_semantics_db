import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv

import config
from divine_semantics_db.scripts.utils import get_or_create_id_sqlite

# Load environment variables
load_dotenv()

# SQLite database file (same as previous scripts)
DB_FILE = config.DB_PATH

# Load CSV
EXCEL_FILE = os.path.join(config.APP_DIR, "data/outlines.csv")
df = pd.read_csv(EXCEL_FILE, sep=";", encoding="utf-8")

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Insert data into the database
    for _, row in df.iterrows():
        cantica_name = row["cantica"]
        cursor.execute("SELECT id FROM cantica WHERE name=?", (cantica_name,))
        result = cursor.fetchone()
        if result is None:
            print(f"Skipping unknown cantica {cantica_name}")
            continue
        cantica_id = result[0]

        canto = int(row["canto"])
        start_verse = int(row["start_verse"])
        end_verse = int(row["end_verse"])

        author_id = get_or_create_id_sqlite(cursor, "author", "name", row["author"])
        type_id = get_or_create_id_sqlite(cursor, "type", "name", row["type"])

        text = row["text"]
        if text:
            # Use INSERT OR REPLACE instead of ON DUPLICATE KEY UPDATE
            cursor.execute(
                """
                INSERT INTO divine_comedy 
                (cantica_id, canto, start_verse, end_verse, text, author_id, type_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(cantica_id, canto, start_verse, end_verse, author_id, type_id) 
                DO UPDATE SET text = excluded.text
                """,
                (cantica_id, canto, start_verse, end_verse, text, author_id, type_id),
            )

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ CSV data successfully imported into SQLite!")

except sqlite3.Error as err:
    print(f"❌ Error: {err}")
