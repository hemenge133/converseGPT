from faster_whisper import WhisperModel
import speech_recognition as sr
import os

class SpeechRecognizer:
    def __init__(self, ambient_duration=1):
        self.recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=ambient_duration)

    def listen(self, model="medium.en"):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            with open("/tmp/microphone-output.wav", "wb") as f:
                f.write(audio.get_wav_data())
            model = WhisperModel(model_size_or_path=model, device="cuda")
            segments, info = model.transcribe("/tmp/microphone-output.wav", beam_size=5)

            text = ""
            for segment in segments:
                text += segment.text
            os.remove("/tmp/microphone-output.wav")

            return text
