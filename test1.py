import asyncio
import queue
import speech_recognition as sr

# Queue for inter-process communication
audio_queue = asyncio.Queue()
text_queue = asyncio.Queue()

# Function to listen for audio input
async def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("Listening...")
    with microphone as source:
        while True:
            audio = recognizer.listen(source)
            await audio_queue.put(audio)

# Function to process audio as speech-to-text
async def process_audio():
    recognizer = sr.Recognizer()
    
    while True:
        audio = await audio_queue.get()
        try:
            text = recognizer.recognize_google(audio)
            await text_queue.put(text)
        except sr.UnknownValueError:
            await text_queue.put("Could not understand audio")
        except sr.RequestError as e:
            await text_queue.put(f"Error: {e}")

# Function to provide text output
async def text_output():
    while True:
        text = await text_queue.get()
        print("User said:", text)
        # Process the text and provide a response to the user

async def main():
    await asyncio.gather(listen(), process_audio(), text_output())

asyncio.run(main())
