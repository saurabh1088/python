import sqlite3

conn = sqlite3.connect("mydb_v1.sqlite")
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

