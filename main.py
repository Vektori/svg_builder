from fastapi import FastAPI
import requests

# Use fastapi to create a simple web server
app = FastAPI()

url = "http://127.0.0.1:11434/api/chat"  # 127.0.0.1 avoids some Windows localhost quirks

# New endpoint to handle requests from Power Automate
@app.post("/powerautomate")
async def powerautomate_endpoint(prompt: dict):
    session = requests.Session()
    session.trust_env = False
    
    payload = {
        "model": "qwen2.5-coder:14b",
        "messages": [{"role": "user", "content": prompt['message']}],
        "stream": False
    }
    
    r = session.post(url, json=payload, timeout=120)
    
    if r.status_code == 200:
        return {"answer": r.json()["message"]["content"]}
    else:
        return {"error": r.text}

# home page
# http://127.0.0.1:8000/docs


