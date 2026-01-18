# SQLite Playground

A Python project exploring various SQLite database concepts through concept-driven examples.

## Prerequisites

- Python 3.x installed on your system
- No additional packages required (uses built-in `sqlite3` module)

## Project Structure

```
sqlite_playground/
├── src/                    # Python concept files
│   └── basic_operations.py # Basic CRUD operations example
├── database/               # SQLite database files
│   └── mydb_v1.sqlite     # Database file (created automatically)
└── README.md              # This file
```

## What This Project Does

This project demonstrates SQLite database concepts through multiple example files:
- **basic_operations.py**: Demonstrates basic CRUD operations
  - Creates a database file (`mydb_v1.sqlite`)
  - Creates an `employee` table with columns: `id`, `name`, `email`, and `designation`
  - Inserts sample employee data
  - Queries and displays all employee records

## Steps to Run

1. **Navigate to the project directory:**
   ```bash
   cd /Users/saurabhverma/DevBox/python/projects/sqlite_playground
   ```

2. **Run a concept file:**
   ```bash
   python src/basic_operations.py
   ```

   Or if you're using Python 3 specifically:
   ```bash
   python3 src/basic_operations.py
   ```

3. **Expected Output:**
   ```
   [(1, 'John Doe', 'john@example.com', 'CEO'), (2, 'Jane Smith', 'jane@example.com', 'CTO')]
   ```

## Database Files

- All database files are stored in the `database/` folder
- Database files are created automatically when scripts are run
- The `database/` folder keeps all database files organized and separate from source code

## Adding New Concepts

To add a new concept file:
1. Create a new Python file in the `src/` folder with a descriptive name (e.g., `transactions.py`, `joins.py`, `indexes.py`)
2. Use the same database path pattern:
   ```python
   import os
   project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   db_path = os.path.join(project_root, "database", "your_db_name.sqlite")
   ```
3. Run it with: `python src/your_concept_file.py`

## Notes

- Scripts use `CREATE TABLE IF NOT EXISTS`, so they're safe to run multiple times
- Scripts use `INSERT OR IGNORE` to prevent duplicate entries
- Each concept file can explore different database concepts independently
