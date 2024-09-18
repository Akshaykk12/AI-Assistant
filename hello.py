import speech_recognition as sr
import pyttsx3
import openai
import os
import time
import google.generativeai as genai

# openai.api_key = ""
genai.configure(api_key=os.getenv("API_KEY"))

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  
engine.setProperty("rate", 150)

activation_command = "Helix"

# def generate_response(prompt):
#     response = openai.Completion.create(
#         model="text-ada-001", prompt=prompt, max_tokens=100, n=1, stop=None, temperature=0.5
#     )
#     return response.choices[0].text.strip()

def generate_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


r = sr.Recognizer()


mic = sr.Microphone()


def listen():
    with mic as source:
        start_time = time.time()
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        end_time = time.time()
        print("Processing...")
        # print(type(audio))

    try:
        text = r.recognize_google(audio)
        end2 = time.time()
        print(f"You said: {text}")
        print(end_time-start_time, end2-end_time)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    # pyttsx3.speak("Press enter to activate ChatGPT...")
    
    print("Listening for activation command...")
    activation_text = listen()
    
    if activation_command.lower() in activation_text.lower():
        print("Activated!")
        speak("Hello, how can I assist you?")

        while True:
            user_input = listen()
            if user_input:
                response = generate_response(user_input)
                print(f"ChatGPT: {response}")
                speak(response)
            else:
                break
    else:
        print("Activation command not recognized.")
