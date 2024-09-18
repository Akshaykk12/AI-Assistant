import speech_recognition as sr
import threading
import time

audio_queue = []
text_queue = []

def listen():
    print("Function a is running at time: " + str(int(time.time())) + " seconds.")
    while True:
        print("Listening...")
        mic = sr.Microphone()
        r = sr.Recognizer()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            audio_queue.append(audio)
            time.sleep(0.5)

def process():
    print("Function b is running at time: " + str(int(time.time())) + " seconds.")
    r = sr.Recognizer()
    while True:
        if audio_queue:
            audio = audio_queue.pop(0)
            text = r.recognize_google(audio)
            text_queue.append(text)

def text_output():
    print("Function c is running at time: " + str(int(time.time())) + " seconds.")
    while True:
        if text_queue:
            text = text_queue.pop(0)
            print(text)

threading.Thread(target=listen).start()
threading.Thread(target=process).start()
threading.Thread(target=text_output).start()
