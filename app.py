from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

# Initialize the Mistral model
model = ollama.Model("mistral")

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get the data from the request
        data = request.json
        text = data['text']
        target_language = data['target_language']

        # Use the Mistral model to translate the text
        translated_text = model.translate(text, target_language)

        # Return the translated text as a JSON response
        return jsonify({'translated_text': translated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

