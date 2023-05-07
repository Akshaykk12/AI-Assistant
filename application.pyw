import speech_recognition as sr
import pyttsx3
import openai
import os

# Replace with your OpenAI API key
openai.api_key = "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"

# Set up text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Change to desired voice
engine.setProperty("rate", 150)

# Define activation command
activation_command = "Helix"

# Define function to generate response from OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=100, n=1, stop=None, temperature=0.5
    )
    return response.choices[0].text.strip()

# Set up speech recognition
r = sr.Recognizer()

# Set microphone as source
mic = sr.Microphone()

# Define function to listen for user input
def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Processing...")

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Define function to speak response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    pyttsx3.speak("Press enter to activate ChatGPT...")
    
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
