from flask import Flask, request, jsonify, make_response
import logging
from initChat import initChat
from flask_cors import CORS
from flask import send_from_directory
from flask_apscheduler import APScheduler
from datetime import datetime

application = Flask(__name__)
CORS(application)
scheduler = APScheduler()
scheduler.init_app(application)
scheduler.start()

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

sessions = {} # Dictionary to store user sessions keyed by OPENAI API key

def check_inactive_sessions():
    now = datetime.now()
    keys_to_remove = []
    for key, session in sessions.items():
        if (now - session['last_activity']).seconds > 300: # 5 minutes
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del sessions[key]
        print("Session for " + key + " terminated")

scheduler.add_job(id='Session Timeout', func=check_inactive_sessions, trigger='interval', seconds=60)

@application.before_request
def log_request_info():
    application.logger.debug('Headers: %s', request.headers)
    application.logger.debug('Body: %s', request.get_data())

@application.route('/', methods=['GET'])
def serve_homepage():
    return send_from_directory('.', 'index.html')

@application.route('/favicon.ico')
def serve_favicon():
    return send_from_directory('.', 'favicon.ico')

@application.route('/send_message', methods=['POST'])
def send_message():
    api_key = request.json.get('api_key')
    user_message = request.json.get('message')
    if api_key not in sessions:
        return make_response("Session not found, try refreshing", 404)
    session = sessions[api_key]
    response = session['conversation']({"message": user_message})["text"]
    return jsonify({'response': response})

@application.route('/reset_chat_agent', methods=['POST'])
def reset_chat_agent():
    api_key = request.json.get('api_key')
    if api_key not in sessions:
        memory, conversation = initChat(api_key)
        sessions[api_key] = {'memory': memory, 'conversation': conversation, 'last_activity': datetime.now()}
        return make_response("Session Initialized", 200)
    else:
        sessions[api_key]['memory'].clear()
        sessions[api_key]['last_activity'] = datetime.now()
        return make_response("Session reset", 200)
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)