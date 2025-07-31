from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/chat"  # Ollama 的本地聊天接口

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    prompt = data.get("prompt", "")
    model = data.get("model", "deepseek-r1:1.5b")

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify({"response": result["message"]["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
