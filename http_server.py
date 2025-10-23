from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ToolRequest(BaseModel):
    sentence: str

@app.get("/")
async def root():
    return {"message": "MCP HTTP Server"}

@app.post("/count_r")
async def count_r(request: ToolRequest):
    print(f"count_r called with sentence: {request.sentence}")
    count = request.sentence.lower().count("r")
    return {"result": count}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)