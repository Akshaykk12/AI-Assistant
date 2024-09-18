import speech_recognition as sr
import threading
import time

# Set up speech recognition
r = sr.Recognizer()
start_time = time.time()

def open_microphone1():
    mic = sr.Microphone()
    end_time=0
    # while True:
    with mic as source:
        start_time = time.time()
            # print(start_time-end_time)
        r.adjust_for_ambient_noise(source)
            
        while time.time() - start_time < 2:
            audio = r.listen(source,phrase_time_limit=2)
            threading.Thread(target=open_microphone1).start()
                # mid_time=time.time()
                # print(mid_time-start_time)
                # print("Processing...")
            try:
                text = r.recognize_google(audio)

                # end_time = time.time()
                print(f"You said: {text}", start_time- time.time())
                # print(end_time-start_time)
            except sr.UnknownValueError:
                    # print("Could not understand audio")
                pass
            except sr.RequestError as e:
                print(f"Error: {e}")

def open_microphone2():
    mic = sr.Microphone()
    end_time=0
    while True:
        with mic as source:
            start_time = time.time()
            # print(start_time-end_time)
            r.adjust_for_ambient_noise(source)
            
            while time.time() - start_time < 2:
                audio = r.listen(source,phrase_time_limit=2)
                threading.Thread(target=open_microphone3).start()
                mid_time=time.time()
                # print(mid_time-start_time)
                # print("Processing...")
                try:
                    text = r.recognize_google(audio)
                    print(f"You said: {text}")
                    end_time = time.time()
                    print(end_time-start_time)
                except sr.UnknownValueError:
                    # print("Could not understand audio")
                    pass
                except sr.RequestError as e:
                    print(f"Error: {e}")

def open_microphone3():
    mic = sr.Microphone()
    end_time=0
    while True:
        with mic as source:
            start_time = time.time()
            # print(start_time-end_time)
            r.adjust_for_ambient_noise(source)
            
            while time.time() - start_time < 2:
                audio = r.listen(source,phrase_time_limit=2)
                threading.Thread(target=open_microphone1).start()
                mid_time=time.time()
                # print(mid_time-start_time)
                # print("Processing...")
                try:
                    text = r.recognize_google(audio)
                    print(f"You said: {text}")
                    end_time = time.time()
                    print(end_time-start_time)
                except sr.UnknownValueError:
                    # print("Could not understand audio")
                    pass
                except sr.RequestError as e:
                    print(f"Error: {e}")

def listen():
    print("Microphone opened. Listening...")
    print("Function a is running at time: " + str(int(time.time())) + " seconds.")
    open_microphone1()


threading.Thread(target=listen).start()
