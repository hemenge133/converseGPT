from flask import Flask, request, jsonify, make_response
from chatGPT import chat, reset

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    response = chat(user_message)
    return jsonify({'response': response})

@app.route('/reset_chat_agent', methods=['GET'])
def reset_chat_agent():
    reset()
    return make_response("Success", 200)
    
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
