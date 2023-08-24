from gtts import gTTS
import os
import pyaudio
from pydub import AudioSegment
import io

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        song = AudioSegment.from_mp3(file)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(song.sample_width),
            channels = song.channels,
            rate = song.frame_rate,
            output = True
        )
        self.byte_stream = io.BytesIO(song.raw_data)

    def play(self):
        """ Play entire file """
        data = self.byte_stream.read(self.chunk)
        while data:
            self.stream.write(data)
            data = self.byte_stream.read(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()


class Speak:
    def speak(self, text):
        speech = gTTS(text = text, lang="en", slow = False).save("/tmp/text.mp3")
        a = AudioFile("/tmp/text.mp3")
        a.play()
        a.close()
