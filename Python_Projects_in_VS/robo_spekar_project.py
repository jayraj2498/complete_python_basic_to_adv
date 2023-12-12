import pyttsx3                            # import modolue to recognize as appech

if __name__ == "__main__":           # <-- here we are in main prog


    print("Welcome to RoboSpeaker, created by J")

    text_to_speak = input("Enter the text you want me to say: ")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 125)  # Speed of speech

    # Speak the given text
    engine.say(text_to_speak)