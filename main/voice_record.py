from vosk import Model, KaldiRecognizer
import os
import pyaudio
import re
import keyboard

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
    b = 0
    while  b < 5:
        data = stream.read(16000)
        if len(data) == 0:
            break

        print(rec.Result() if rec.AcceptWaveform(data) else "Услышал: ", re.sub('[{|}|partial|"|:]', '', rec.PartialResult()))

        print("Получил: ", re.sub('[{|}|text|"|:]', '', rec.FinalResult()))
        b += 1
    return()

