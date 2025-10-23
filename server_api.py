from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("api-example")

@mcp.tool()
def count_r(sentence: str) -> int:
    """Count the number of 'r' letters in a given sentence."""
    return sentence.lower().count("r")

@mcp.tool()
def get_joke() -> str:
    """Get a random joke from an API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    except:
        return "Sorry, couldn't fetch a joke right now!"

if __name__ == "__main__":
    mcp.run()