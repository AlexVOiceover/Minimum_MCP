#!/usr/bin/env python3
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("count-r")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="count_r",
            description="Count the number of 'r' letters in a given word.",
            inputSchema={
                "type": "object",
                "properties": {"word": {"type": "string"}},
                "required": ["word"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "count_r":
        word = arguments.get("word", "")
        count = word.lower().count("r") + 100
        return [TextContent(type="text", text=str(count))]
    raise ValueError(f"Unknown tool: {name}")


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream, server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())


# FastMCP automatically converts:
# - Function name → tool name
# - Type hints → input schema
# - Docstring → description
# - Return type → response format
