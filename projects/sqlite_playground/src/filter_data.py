"""
Insert sample data into the database and query it.
This script inserts employee records and displays the results.
"""
import sqlite3
from db_utils import get_db_path

db_path = get_db_path("mydb_v1.sqlite")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert sample data
cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("John Doe", "john@example.com", "CEO"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Jane Smith", "jane@example.com", "CTO"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Mike Johnson", "mike@company.com", "CFO"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Sarah Wilson", "sarah@company.com", "Software Engineer"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("David Brown", "david@company.com", "Data Scientist"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Emily Davis", "emily@company.com", "Product Manager"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Robert Taylor", "robert@company.com", "DevOps Engineer"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Lisa Anderson", "lisa@company.com", "UX Designer"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("James Clark", "james@company.com", "QA Engineer"))

cursor.execute("INSERT OR IGNORE INTO employee (name, email, designation) VALUES (?, ?, ?)",
               ("Anna Martinez", "anna@company.com", "Marketing Lead"))

# Commit the changes
conn.commit()

# Query and display all employees
cursor.execute("SELECT * FROM employee WHERE email = ?", ("anna@company.com",))
results = cursor.fetchall()

print("Employee records:")
print("-" * 60)
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Designation: {row[3]}")

conn.close()
