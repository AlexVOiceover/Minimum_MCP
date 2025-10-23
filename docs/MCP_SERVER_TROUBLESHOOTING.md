# MCP Server Fix

**Problem**: `ModuleNotFoundError: No module named 'mcp'` - Claude Desktop was using system Python instead of virtual environment.

**Solution**: Use full path to venv Python in config: `"/path/to/.venv/bin/python3"` instead of just `"python3"`.