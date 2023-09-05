from flask import Flask, request, jsonify, make_response, session
from flask_session import Session
import logging
from initChat import initChat
from flask import send_from_directory
import redis

application = Flask(__name__)

"""
TODO: Tests are currently only being run from the client side. Errors on the server side will still successfully deploy which is not ideal. There should just be a server specific test file and we'll run pytest on the server as well.
"""

"""
Setup redis session cache
"""
SESSION_TYPE = 'redis'
SESSION_PERMANENT = False # Close session when browser closes
SESSION_USE_SIGNER = True # Encrypt the session cookie
SESSION_KEY_PREFIX = 'redis_alpha:'
SESSION_REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
application.config.from_object(__name__)
Session(application)

"""
Log all request info
"""
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)

@application.before_request
def log_request_info():
    application.logger.debug('Headers: %s', request.headers)
    application.logger.debug('Body: %s', request.get_data())

"""
Serve Homepage / favicon
"""
@application.route('/', methods=['GET'])
def serve_homepage():
    return send_from_directory('.', 'index.html')

@application.route('/favicon.ico')
def serve_favicon():
    return send_from_directory('.', 'favicon.ico')

"""
Send a message to the current chat agent.
"""
@application.route('/send_message', methods=['POST'])
def send_message():
    api_key = request.json.get('api_key', None)
    if not api_key:
        return make_response("OpenAI API Key not found", 400)
    user_message = request.json.get('message', "")
    response = session['conversation']({"message": user_message})["text"]
    return jsonify({'response': response})

"""
Init the chat agent with a fresh memory. Page reload also triggers reset_chat_agent.
"""
@application.route('/reset_chat_agent', methods=['POST'])
def reset_chat_agent():
    api_key = request.json.get('api_key', None)
    if not api_key:
        return make_response("OpenAI API Key not found", 400)
    try:
        memory, conversation = initChat(api_key)
        session['memory'] = memory
        session['conversation'] = conversation
        return make_response("Session Initialized", 200)
    except:
        return make_response("Internal Server Error", 500)
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
