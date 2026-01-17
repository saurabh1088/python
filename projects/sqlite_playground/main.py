import sqlite3

conn = sqlite3.connect("mydb.sqlite")
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    )
""")

# Insert some sample data (optional)
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ("Jane Smith", "jane@example.com"))

# Commit the changes
conn.commit()

# Now query the users table
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()

