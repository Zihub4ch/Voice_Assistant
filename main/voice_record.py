from vosk import Model, KaldiRecognizer
import os
import pyaudio
import re
import keyboard
import time

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
        # print(rec.Result() if rec.AcceptWaveform(data) else "Услышал: ", re.sub('[{|}|partial|"|:]', '', rec.PartialResult()))
        # print("Получил: ", re.sub('[{|}|text|"|:]', '', rec.FinalResult()))
        text = rec.Result() if rec.AcceptWaveform(data) else "Услышал: ", re.sub('[{|}|partial|"|:]', '', rec.PartialResult())  
        return(text)
    
def commands():
    while True:
        text = list(Record())
        text_to_str = ' '.join(text)
        text_filt = re.sub('[{|}|text|"|:]', '', text_to_str) 
        print("Получил: ", text_filt)
        
        if "скрин" in text_filt:
            keyboard.press('win+shift+s')
            time.sleep(0.1)
            keyboard.release('win+shift+s')
        
        elif "поставь" in text_filt:
            keyboard.press('ctrl+v')
            time.sleep(0.05)
            keyboard.release('ctrl+v')

commands() 