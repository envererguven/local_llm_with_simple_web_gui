from flask import Flask, request, jsonify, send_file
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('ollama_llm.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')
    ollama_url = 'http://127.0.0.1:11434/api/generate'
    payload = {
        'model': 'llama3.2:1b',
        'prompt': prompt
    }
    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()
        # Ollama may return multiple JSON objects (streaming)
        first_line = response.text.splitlines()[0]
        result = ''
        try:
            result = json.loads(first_line).get('response', '')
        except Exception as e:
            return jsonify({'error': f'JSON parse error: {str(e)}'}), 500
        return jsonify({'response': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
