import json
import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv

import config

# SQLite database file
DB_FILE = config.DB_FILE

# Load CSV
EXCEL_FILE = os.path.join(config.APP_DIR, "data/mappings.csv")  # Adjust if needed
df = pd.read_csv(EXCEL_FILE, sep=";", encoding="utf-8")


try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS verse_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantica_id INTEGER,
            canto INTEGER,
            start_verse INTEGER,
            end_verse INTEGER,
            cumulative_indices TEXT,
            UNIQUE(cantica_id, canto, start_verse, end_verse)
        )"""
    )

    for _, row in df.iterrows():
        cantica_id = int(row["cantica_id"])
        if cantica_id is None:
            print(f"Skipping unknown cantica: {row['cantica']}")
            continue

        canto = int(row["canto"])
        cumulative_indices_json = json.dumps(row["cumulative_indices"])

        start_verse, end_verse = map(int, row["verse"].split("-"))

        cursor.execute(
            """INSERT INTO verse_mappings 
            (cantica_id, canto, start_verse, end_verse, cumulative_indices)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(cantica_id, canto, start_verse, end_verse) 
            DO UPDATE SET cumulative_indices = excluded.cumulative_indices
            """,
            (cantica_id, canto, start_verse, end_verse, cumulative_indices_json),
        )

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ CSV data successfully imported into SQLite!")

except sqlite3.Error as err:
    print(f"❌ Error: {err}")


# df.to_sql("verse_mappings", conn, if_exists="replace", index=False)
#
# conn.close()