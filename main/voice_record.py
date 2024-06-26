from vosk import Model, KaldiRecognizer
import os
import pyaudio
import re
import time
import keyboard
import webbrowser
import subprocess
import pyautogui

model = Model(r"C:/Users/User/Desktop/PROG/.vscode/voice_helper/vosk-model-small-ru-0.22") # полный путь к модели
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()


stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=16000, 
    input=True, 
    frames_per_buffer=16000
)
stream.start_stream()


def Record():
    while True:
        data = stream.read(16000)
        if len(data) == 0:
            break
        text = rec.Result() if rec.AcceptWaveform(data) else "", re.sub('[{|}|partial|"|:]', '', rec.PartialResult())  
        return(text)
    
def commands():
    while True:
        text = list(Record())
        text_to_str = ' '.join(text)
        text_filt = re.sub('[{|}|text|"|:]', '', text_to_str) 
        print("Получил: ", text_filt)
        
        if "скрин" in text_filt or "скриншот" in  text_filt:
            keyboard.press_and_release("win+shift+s")
        
        elif "вставь" in text_filt or "вставить" in text_filt or "ставить" in text_filt:
            keyboard.press_and_release("ctrl+v")
        
        elif "браузер" in text_filt:
            browser_path = "C:/Users/User/AppData/Local/Programs/Opera GX/launcher.exe"
            webbrowser.register('operaGX', None, webbrowser.BackgroundBrowser(browser_path))
            url = "https://ya.ru"
            webbrowser.get('operaGX',).open(url)
        
        elif "телеграм" in text_filt:
            telegram_path = "C:/Users/User/AppData/Roaming/Telegram Desktop/Telegram.exe"
            subprocess.call([telegram_path])

commands() 