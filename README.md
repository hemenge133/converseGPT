# converseGPT
## Talk to chatgpt (with langchain) using faster-whisper for STT and google TTS
![alt text](https://github.com/hemenge133/converseGPT/blob/main/ss_dark.png?raw=true)
![alt text](https://github.com/hemenge133/converseGPT/blob/main/ss_light.png?raw=true)

# Prerequisites
- Add your OpenAI API key to a file called .env
```
OPENAI_API_KEY="sk-***"
```

# Quickstart STT/TTS Console Application
## (using Ubuntu2004, CUDA enabled)

### Install Dependencies
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-pyaudio ffmpeg libcudnn8 flask flask-cors
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Console-Based STT / TTS conversation with chatGPT (Disabled while I get testing working for audio stuff)
```
python chatGPT.py
```

# Text only web UI similar to chatGPT
```
python server.py &
open index.html
```
