import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MarkdownNotes")
NOTES_DIRECTORY = os.path.expanduser("~/DevBox/notes")

@mcp.tool()
def list_notes() -> list[str]:
    """Recursively lists all markdown files in the notes folder and all subfolders."""
    markdown_files = []
    
    # os.walk traverses the entire directory tree
    for root, dirs, files in os.walk(NOTES_DIRECTORY):
        for file in files:
            if file.endswith(".md"):
                # Calculate the relative path from the base notes directory
                relative_path = os.path.relpath(os.path.join(root, file), NOTES_DIRECTORY)
                markdown_files.append(relative_path)
                
    return markdown_files

@mcp.tool()
def read_note(relative_path: str) -> str:
    """Reads a note using its relative path (e.g., 'ProjectA/meeting.md')."""
    # Security: Ensure the path is within the notes directory
    full_path = os.path.abspath(os.path.join(NOTES_DIRECTORY, relative_path))
    
    if not full_path.startswith(os.path.abspath(NOTES_DIRECTORY)):
        return "Error: Access denied. Path is outside of notes directory."
    
    if not os.path.exists(full_path):
        return f"Error: File {relative_path} not found."
    
    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    mcp.run()
