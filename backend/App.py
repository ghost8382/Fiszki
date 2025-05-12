from flask import Flask, request, jsonify
from Extractor import extract_text
from generator import generate_flashcards

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    text = extract_text(file)
    flashcards = generate_flashcards(text)
    return jsonify(flashcards)

if __name__ == '__main__':
    app.run(debug=True)