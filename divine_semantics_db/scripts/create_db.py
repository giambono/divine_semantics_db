import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME")

# Connect without specifying a database
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


cursor = conn.cursor()

# Create database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")

print(f"✅ Database '{DB_NAME}' created successfully!")

cursor.close()
conn.close()
