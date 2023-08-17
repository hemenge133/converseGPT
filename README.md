# converseGPT
## Talk to chatgpt (with langchain) using faster-whisper for STT and google TTS

# Prerequisites
- Add your OpenAI API key to a file called .env
```
OPENAI_API_KEY="sk-***"
```

# Quickstart STT/TTS Console Application
## (using Ubuntu2004, CUDA enabled)
```
sudo apt install portaudio19-dev python3-pyaudio ffmpeg libcudnn8
pip install -r requirements.txt
python chatGPT.py
```

# Text only web UI similar to chatGPT
```
https://www.metacareers.com/jobs/3157358737902887/?rx_campaign=Linkedin1&rx_ch=connector&rx_group=126320&rx_job=a1K2K000008UcfbUAC_3275bd43&rx_medium=post&rx_r=none&rx_source=Linkedin&rx_ts=20230816T184802Z&rx_vp=slots&utm_campaign=Job%2Bboard&utm_medium=jobs&utm_source=LIpaid&rx_viewer=b85f7a793c9611eeb2b1a3c8c82ecb8f06bdb93de3214d0e8ff2048d1e639568
python server.py
open index.html
```
