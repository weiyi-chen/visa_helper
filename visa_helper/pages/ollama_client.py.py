import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

def ask_deepseek(prompt, model="deepseek-r1:1.5b"):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    resp = requests.post(OLLAMA_URL, json=payload)
    resp.raise_for_status()
    return resp.json()["message"]["content"]