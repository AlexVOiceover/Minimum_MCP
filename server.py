from mcp.server.fastmcp import FastMCP

mcp = FastMCP("count-r")

@mcp.tool()
def count_r(word: str) -> int:
    """Count the number of 'r' letters in a given word."""
    return word.lower().count("r")

if __name__ == "__main__":
    mcp.run()
