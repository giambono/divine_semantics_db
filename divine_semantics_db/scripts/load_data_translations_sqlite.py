import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv

import config
from divine_semantics_db.scripts.utils import get_or_create_id_sqlite

TYPE = "TEXT"

# Load environment variables
load_dotenv()

# SQLite database file (same as previous scripts)
DB_FILE = os.path.join(config.APP_DIR, "data/divine_comedy.db")

# Load CSV
EXCEL_FILE = os.path.join(config.APP_DIR, "data/translations.xlsx")
df = pd.read_excel(EXCEL_FILE)

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Ensure type exists in the database
    type_id = get_or_create_id_sqlite(cursor, "type", "name", TYPE)

    for _, row in df.iterrows():
        cantica_id = config.CANTICA_MAP.get(row["cantica"], None)
        if cantica_id is None:
            print(f"Skipping unknown cantica: {row['cantica']}")
            continue

        canto = int(row["canto"])
        start_verse, end_verse = map(int, row["verse"].split("-"))
        author_id = get_or_create_id_sqlite(cursor, "author", "name", row["author"])
        text = row["text"]

        if text:
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
