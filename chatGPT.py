from langchain.schema import HumanMessage, AIMessage, SystemMessage
from record import SpeechRecognizer
from speak import Speak
import os
from langchain.chat_models import ChatOpenAI
from ctypes import *
from contextlib import contextmanager
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory 

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

systemprompt="You are a helpful assistant."

model_kwargs = {"top_p": 1, "frequency_penalty": 0.1, "presence_penalty": 0.1}

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, model_kwargs=model_kwargs)

with noalsaerr():
    listen = SpeechRecognizer()
    speak = Speak()

prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(systemprompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{message}")
        ]
    )

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory
)


"""
Simple single-user API for now. POST at http:server-ip:5000/send_message
"""
def chat(message):
    response = conversation({"message": message})
    return response["text"]

"""
Reset the chat if the page is reloaded
"""
def reset():
    memory.clear()

"""
Running this module as the main function ie. `python chatGPT.py` will launch converseGPT with STT/TTS
"""
def main():
    print("ready")
    while True:
        with noalsaerr():
            message = listen.listen()
        response = conversation({"message": message})
        response = response["text"]
        with noalsaerr():
            speak.speak(response)

if __name__ == "__main__":
    main()
