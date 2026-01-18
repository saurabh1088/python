# SQLite Playground

A Python project exploring various SQLite database concepts through concept-driven examples.

## Prerequisites

- Python 3.x installed on your system
- No additional packages required (uses built-in `sqlite3` module)

## Project Structure

```
sqlite_playground/
├── src/                    # Python concept files
│   ├── db_utils.py        # Utility module for database path management
│   ├── create_database.py # Creates database and table structure
│   └── insert_data.py     # Inserts sample data and queries records
├── database/               # SQLite database files
│   └── mydb_v1.sqlite     # Database file (created automatically)
└── README.md              # This file
```

## What This Project Does

This project demonstrates SQLite database concepts through multiple example files:
- **db_utils.py**: Utility module providing a helper function to get database paths
- **create_database.py**: Creates the database file and defines the table schema
  - Creates a database file (`mydb_v1.sqlite`)
  - Creates an `employee` table with columns: `id`, `name`, `email`, and `designation`
- **insert_data.py**: Inserts sample data and queries records
  - Inserts sample employee data
  - Queries and displays all employee records

## Steps to Run

1. **Navigate to the project directory:**
   ```bash
   cd /Users/saurabhverma/DevBox/python/projects/sqlite_playground
   ```

2. **Create the database and table structure:**
   ```bash
   python src/create_database.py
   ```
   
   Or if you're using Python 3 specifically:
   ```bash
   python3 src/create_database.py
   ```
   
   Expected output:
   ```
   Database created successfully at: /path/to/database/mydb_v1.sqlite
   Table 'employee' created with columns: id, name, email, designation
   ```

3. **Insert data and query records:**
   ```bash
   python src/insert_data.py
   ```
   
   Or:
   ```bash
   python3 src/insert_data.py
   ```
   
   Expected output:
   ```
   Employee records:
   ------------------------------------------------------------
   ID: 1, Name: John Doe, Email: john@example.com, Designation: CEO
   ID: 2, Name: Jane Smith, Email: jane@example.com, Designation: CTO
   ```

## Database Files

- All database files are stored in the `database/` folder
- Database files are created automatically when scripts are run
- The `database/` folder keeps all database files organized and separate from source code

## Adding New Concepts

To add a new concept file:
1. Create a new Python file in the `src/` folder with a descriptive name (e.g., `transactions.py`, `joins.py`, `indexes.py`)
2. Import the database utility helper:
   ```python
   from db_utils import get_db_path
   db_path = get_db_path("your_db_name.sqlite")
   ```
   Or use a custom database name:
   ```python
   from db_utils import get_db_path
   db_path = get_db_path("custom_database.sqlite")
   ```
3. Run it with: `python src/your_concept_file.py`

## Notes

- Scripts use `CREATE TABLE IF NOT EXISTS`, so they're safe to run multiple times
- Scripts use `INSERT OR IGNORE` to prevent duplicate entries
- Each concept file can explore different database concepts independently
