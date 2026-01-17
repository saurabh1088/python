# SQLite Playground

A simple Python project demonstrating SQLite database operations.

## Prerequisites

- Python 3.x installed on your system
- No additional packages required (uses built-in `sqlite3` module)

## Project Structure

```
sqlite_playground/
├── main.py          # Main script with SQLite operations
└── README.md        # This file
```

## What This Project Does

This project demonstrates basic SQLite database operations:
- Creates a database file (`mydb_v1.sqlite`)
- Creates an `employee` table with columns: `id`, `name`, `email`, and `designation`
- Inserts sample employee data
- Queries and displays all employee records

## Steps to Run

1. **Navigate to the project directory:**
   ```bash
   cd /Users/saurabhverma/DevBox/python/projects/sqlite_playground
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

   Or if you're using Python 3 specifically:
   ```bash
   python3 main.py
   ```

3. **Expected Output:**
   ```
   [(1, 'John Doe', 'john@example.com', 'CEO'), (2, 'Jane Smith', 'jane@example.com', 'CTO')]
   ```

## Database File

- The script creates a SQLite database file named `mydb_v1.sqlite` in the same directory as `main.py`
- The database file will be created automatically on first run
- Subsequent runs will use the existing database and won't duplicate data (thanks to `INSERT OR IGNORE`)

## Notes

- The script uses `CREATE TABLE IF NOT EXISTS`, so it's safe to run multiple times
- The script uses `INSERT OR IGNORE` to prevent duplicate entries
- You can modify `main.py` to add more operations or change the database schema
