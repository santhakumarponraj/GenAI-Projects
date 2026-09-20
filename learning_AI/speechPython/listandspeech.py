import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Listening... Speak into your microphone.")
    
    # Adjust for ambient background noise
    recognizer.adjust_for_ambient_noise(source, duration=1)
    
    # Record the audio
    audio = recognizer.listen(source)

try:
    print("Recognizing speech...")
    # Convert audio to text using Google's free web service
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Could not request results; check your internet connection.")
