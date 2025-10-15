import wikipedia
import wolframalpha
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)  

# Get Wolfram Alpha API key
wolfram_app_id = os.getenv("WOLFRAM_APP_ID")
if not wolfram_app_id:
    raise ValueError("WOLFRAM_APP_ID not found in .env file")
wolfram_client = wolframalpha.Client(wolfram_app_id)  

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None

def process_query(query):
    try:
        res = wolfram_client.query(query)
        answer = next(res.results).text
        speak("According to Wolfram Alpha:")
        speak(answer)
    except Exception:
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Your query is too ambiguous. Try being more specific.")
        except Exception:
            speak("Sorry, I couldn't find anything related to your query.")

# Main loop
def main():
    speak("Hi, I am your virtual assistant. How can I help you?")
    while True:
        query = get_audio()
        if query:
            if 'exit' in query or 'stop' in query:
                speak("Goodbye!")
                break
            process_query(query)

if __name__ == "__main__":
    main()
