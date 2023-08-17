# converseGPT
## Talk to chatgpt (with langchain) using faster-whisper for STT and google TTS

# Prerequisites
- Add your OpenAI API key to a file called .env
```
OPENAI_API_KEY="sk-***"
```

# Quickstart STT/TTS Console Application (using Ubuntu2004, CUDA enabled)
```
sudo apt install portaudio19-dev python3-pyaudio ffmpeg libcudnn8
pip install -r requirements.txt
python chatGPT.py
```

# Text only web UI similar to chatGPT
```
python server.py
```
And open index.html with your web browser
