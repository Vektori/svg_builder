import requests
import json

#%%
url = "http://localhost:11434/api/chat"

payload = {
    "model": "qwen2.5-coder:14b",
    "messages": [
        {
            "role": "user",
            "content": "Write a Python function that calculates the factorial of a number using recursion."
        }
    ]
}

response = requests.post(url, json=payload, stream=True)



# %%
