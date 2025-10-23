from mcp.server.fastmcp import FastMCP

mcp = FastMCP("count-r")


@mcp.tool()
def count_r(sentence: str) -> int:
    """Count the number of 'r' letters in a given sentence.
    Args:
        sentence (str): The sentence to analyze.
    Returns:
        int: The count of 'r' letters in the sentence.
    """
    return sentence.lower().count("r")


if __name__ == "__main__":
    mcp.run()
