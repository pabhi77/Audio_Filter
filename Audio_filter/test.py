

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
    print("Audio captured!")

try:
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
