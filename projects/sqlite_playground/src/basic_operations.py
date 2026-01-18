import sqlite3
import os

# Get the project root directory (parent of src/)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "database", "mydb_v1.sqlite")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        designation TEXT
    )
""")

# Insert some sample data (optional)
cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)", ("John Doe", "john@example.com", "CEO"))
cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)", ("Jane Smith", "jane@example.com", "CTO"))

# Commit the changes
conn.commit()

# Now query the users table
cursor.execute("SELECT * FROM employee")
print(cursor.fetchall())

conn.close()
