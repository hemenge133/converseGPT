from langchain.schema import HumanMessage, AIMessage, SystemMessage
from record import SpeechRecognizer
from speak import Speak
import os
from langchain.chat_models import ChatOpenAI
from ctypes import *
from contextlib import contextmanager

from dotenv import load_dotenv

load_dotenv()
# Get rid of annoying ALSA errors 
@contextmanager
def noalsaerr():
    ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

    def py_error_handler(filename, line, function, err, fmt):
        pass

    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

# Model Inputs / Variables

systemprompt="AI will track food intake, figuring out the user's intake for the day in calorie and macronutrient counts. In every message AI will output the totals for the conversation like this: \"Protein: Xg Carbs: Xg Fat: Xg Calories: X.\" The only output besides that format will be to ask clarifying questions on food type, quantity, etc. AI will infer quantities based on what a normal serving is. The AI will respond without prose or explaination, quantities and questions only."

model_kwargs = {"top_p": 1, "frequency_penalty": 0.1, "presence_penalty": 0.1}

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, model_kwargs=model_kwargs)

with noalsaerr():
    listen = SpeechRecognizer()
    speak = Speak()

messages = [
    SystemMessage(content=systemprompt)
]

print("ready")
while True:
    with noalsaerr():
        message = listen.listen()
    print("Me: " + message)    

    messages.append(HumanMessage(content=message))
    response = chat.predict_messages(messages).content

    with noalsaerr():
        speak.speak(response)

    print("ChatGPT: " + response)
    messages.append((AIMessage(content=response)))
