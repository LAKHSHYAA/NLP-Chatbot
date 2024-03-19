from flask import Flask, request, jsonify
import spacy
import json
import random

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

with open('data.json') as file:
    data = json.load(file)
    intents = data['intents']

@app.route('/')
def home():
    return 'Chatbot is running!'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message']
    response = get_response(message)
    return jsonify({'response': response})

def get_response(message):
    doc = nlp(message)
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in message.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that."

if __name__ == '__main__':
    app.run(debug=True)
