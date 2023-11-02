import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

# List of blacklisted words or phrases
blacklist = ["hot", "black", "shit"]

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def filter_text(text):
    audio_output = AudioSegment.empty()

    for word in blacklist:
        if word in text:
            # Add a beep sound for unwanted words
            print("Beep sound for unwanted word:", word)
            beep = AudioSegment.from_wav("beep.wav")  # Replace with the path to your beep sound file
            audio_output += beep
            text = text.replace(word, "*" * len(word))
        text_to_speech(text)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the Google Web Speech API for speech recognition
with sr.Microphone() as source:
    print("Speak something...")

    # Adjust for ambient noise to reduce initial delay
    recognizer.adjust_for_ambient_noise(source)
    
    try:
        audio = recognizer.listen(source, timeout=10)  # Set a timeout (in seconds)
        recognized_text = recognizer.recognize_google(audio)
        
        # Filter the text and play a beep for unwanted words
        filter_text(recognized_text)
    except sr.WaitTimeoutError:
        print("Speech recognition timed out.")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
