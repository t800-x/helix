import subprocess
import pyttsx3
import openai
import json

def get_api_key():
    with open('config.json') as f:
        data = json.load(f)

    if 'WHISPER_KEY' in data:
        return data['WHISPER_KEY']
    else:
        return None

def record():
    command = 'python ./recorder.py'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print()


def transcribe_wav_file():
    #todo
    transcription = ''

def speech_recognition():
    record()
    transcription = transcribe_wav_file()
    return transcription

def tts(text):
    voice_id='HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()


print(transcribe_wav_file())