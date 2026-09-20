import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Optional: Adjust speed and volume
engine.setProperty('rate', 150)    # Speed of speech (words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Say something
text = "Hello! Your Python code can now speak."
engine.say(text)

# Process and run the speech commands
engine.runAndWait()
