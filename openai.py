import openai

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')
    openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your actual key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message['content']
        return jsonify({'response': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500