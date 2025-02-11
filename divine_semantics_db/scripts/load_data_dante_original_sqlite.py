import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv

import config
from divine_semantics_db.scripts.utils import get_or_create_id_sqlite

AUTHOR = "dante"
TYPE = "TEXT"

# Load environment variables
load_dotenv()

# SQLite database file
DB_FILE = os.path.join(config.APP_DIR, "data/divine_comedy.db")

# Load CSV
EXCEL_FILE = os.path.join(config.APP_DIR, "data/dante_original.xlsx")  # Adjust if needed
df = pd.read_excel(EXCEL_FILE)

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS divine_comedy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantica_id INTEGER,
            canto INTEGER,
            start_verse INTEGER,
            end_verse INTEGER,
            text TEXT,
            author_id INTEGER,
            type_id INTEGER,
            UNIQUE(cantica_id, canto, start_verse, end_verse, author_id, type_id) 
        )"""
    )

    # Ensure author and type exist in the database
    author_id = get_or_create_id_sqlite(cursor, "author", "name", AUTHOR)
    type_id = get_or_create_id_sqlite(cursor, "type", "name", TYPE)

    # Insert translations into the database
    for _, row in df.iterrows():
        cantica_id = config.CANTICA_MAP.get(row["cantica"], None)
        if cantica_id is None:
            print(f"Skipping unknown cantica: {row['cantica']}")
            continue

        canto = int(row["canto"])
        start_verse, end_verse = map(int, row["verse"].split("-"))

        text = row["text"]
        if text:
            cursor.execute(
                """INSERT INTO divine_comedy 
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
