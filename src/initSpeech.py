from record import SpeechRecognizer
from speak import Speak
from contextlib import contextmanager
from ctypes import *
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



def initSpeech():
    with noalsaerr():
        listen = SpeechRecognizer()
        speak = Speak()
    return noalsaerr, SpeechRecognizer, listen, speak