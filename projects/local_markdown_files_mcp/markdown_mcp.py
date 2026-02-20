import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP - the 'Smart Librarian'
mcp = FastMCP("MarkdownNotes")

# Define the path to your notes
NOTES_DIRECTORY = os.path.expanduser("~/Documents/MyNotes")

@mcp.tool()
def list_notes() -> list[str]:
    """Lists all markdown files available in the knowledge base."""
    if not os.path.exists(NOTES_DIRECTORY):
        return [f"Error: Directory {NOTES_DIRECTORY} not found."]
    
    return [f for f in os.listdir(NOTES_DIRECTORY) if f.endswith('.md')]

@mcp.tool()
def read_note(filename: str) -> str:
    """Reads the content of a specific markdown note by filename."""
    # Security: Prevent directory traversal (Senior Step!)
    safe_filename = os.path.basename(filename)
    file_path = os.path.join(NOTES_DIRECTORY, safe_filename)
    
    if not os.path.exists(file_path):
        return f"Error: File {filename} not found."
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    mcp.run()
    