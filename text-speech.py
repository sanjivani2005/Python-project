import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Text to be converted to speech
print(" WElcome to RoboSpeaker 1.0 Created by Sanjii")

while True:
    x= input("Enter what you want me to pronounce :-> ")
    if x == "q":
            break 
    # Use the TTS engine to say the text
    engine.say(x)

    # Wait for the speech to finish
    engine.runAndWait()