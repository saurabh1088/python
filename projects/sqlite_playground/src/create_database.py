"""
Create database and table structure.
This script creates the database file and defines the table schema.
"""
import sqlite3
from db_utils import get_db_path

db_path = get_db_path("mydb_v1.sqlite")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the employee table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        designation TEXT
    )
""")

# Commit the changes
conn.commit()

print(f"Database created successfully at: {db_path}")
print("Table 'employee' created with columns: id, name, email, designation")

conn.close()
