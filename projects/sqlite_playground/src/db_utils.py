"""
Utility module for database path management.
"""
import os

def get_db_path(db_name="mydb_v1.sqlite"):
    """
    Get the absolute path to a database file in the database folder.
    
    Args:
        db_name (str): Name of the database file
        
    Returns:
        str: Absolute path to the database file
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(project_root, "database", db_name)
