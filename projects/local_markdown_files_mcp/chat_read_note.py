import asyncio
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 1. Setup MCP Server Parameters
server_params = StdioServerParameters(
    command="python3",
    args=["markdown_mcp.py"], # Ensure this path is correct
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # 2. Initialize Ollama
            # Make sure you have the model downloaded: ollama pull llama3
            llm = ChatOllama(model="llama3", temperature=0)

            # 3. Fetch Tools from your MCP Server
            tools = await session.list_tools()
            
            # 4. Simple Loop for Interaction
            print("--- Connected to Markdown Notes ---")
            user_input = "Read the contents of note TheMatryoshkaDollModel.md?"
            
            # In a full implementation, you'd use a LangChain Agent here
            # For now, let's manually call the read_note tool
            # NOTE: Here relative_path should be the path to the note you want to read, adjust as necessary
            # TODO: Implement a more dynamic way to determine which note to read based on user input
            response = await session.call_tool("read_note", arguments={"relative_path": "TheMatryoshkaDollModel.md"})
            print(f"Note contents: {response.content}")

if __name__ == "__main__":
    asyncio.run(main())
