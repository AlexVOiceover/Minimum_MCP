from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Connect to the MCP server
    server_params = StdioServerParameters(command="python3", args=["server.py"])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize and discover tools
            await session.initialize()

            # Call the count_r tool
            result = await session.call_tool("count_r", {"word": "strawberry"})
            print(f"Result: {result}")  # Output: Result: 3


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
