from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json

app = FastAPI()

class Query(BaseModel):
    query: str

TOOLS = {
    "calculator": lambda expr: str(eval(expr)),
}

def detect_tool(query: str):
    q = query.lower()
    if any(op in q for op in ["+", "-", "*", "/", "calculate", "what is"]):
        import re
        expr = re.findall(r"[\d\s\+\-\*\/\(\)\.]+", query)
        if expr:
            return "calculator", expr[0].strip()
    return None, None

def ask_tinyllama(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "tinyllama", prompt],
        capture_output=True, text=True, timeout=60
    )
    return result.stdout.strip()

@app.post("/query")
def query(request: Query):
    tool, tool_input = detect_tool(request.query)
    if tool and tool_input:
        try:
            tool_output = TOOLS[tool](tool_input)
            return {
                "query": request.query,
                "tool_used": tool,
                "tool_input": tool_input,
                "result": tool_output
            }
        except Exception as e:
            pass
    response = ask_tinyllama(request.query)
    return {
        "query": request.query,
        "tool_used": None,
        "result": response
    }

@app.get("/")
def root():
    return {"status": "Local LLM Agent running"}
