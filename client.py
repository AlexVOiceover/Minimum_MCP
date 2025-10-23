from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    sentence = input("Enter a sentence to count 'r' letters: ")

    # Configure server launch parameters - MCP uses stdio communication
    server_params = StdioServerParameters(command="python3", args=["server.py"])

    # Step 1: Launch server and get communication pipes
    # Create stdio connection to the server
    stdio_connection = stdio_client(server_params)
    # Launch the server process
    read_pipe, write_pipe = await stdio_connection.__aenter__()

    try:
        # Step 2: Create MCP session using the pipes
        session = ClientSession(read_pipe, write_pipe)
        # Initialize the session
        await session.__aenter__()

        try:
            # Step 3: Initialize and discover tools
            await session.initialize()

            # Step 4: Call the count_r tool
            result = await session.call_tool("count_r", {"sentence": sentence})
            print(f"Result: {result}")
        finally:
            # Step 5: Clean up session
            await session.__aexit__(None, None, None)
    finally:
        # Step 6: Clean up connection
        await stdio_connection.__aexit__(None, None, None)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
