import speech_recognition as sp
import webbrowser
import pyttsx3
import IslamicAudio

# Initialize recognizer and text-to-speech engine
recognizer = sp.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to process commands
import webbrowser
import os

def commandProcess(command):
    command = command.lower()

    # Open websites
    if "open youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
        talk("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif "open stack overflow" in command:
        talk("Opening Stack Overflow")
        webbrowser.open("https://www.stackoverflow.com")

    elif "open wikipedia" in command:
        talk("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")

    elif "open gmail" in command:
        talk("Opening Gmail")
        webbrowser.open("https://www.gmail.com")

    # Open applications (Windows example)
    elif "open notepad" in command:
        talk("Opening Notepad")
        os.system("notepad.exe")

    elif "open word" in command:
        talk("Opening Word")
        os.system("word.exe")

    elif "open calculator" in command:
        talk("Opening Calculator")
        os.system("calc.exe")

    elif "open command prompt" in command:
        talk("Opening Command Prompt")
        os.system("cmd.exe")

    # Search on Google
    elif "search" in command:
        question = command.repace("search ", "").strip()
        talk(f"Searching for {question} on Google")
        webbrowser.open(f"https://www.google.com/search?q={question}")

    # Play naseed on YouTube
    elif "play" in command.lower():
        naat = command.replace("play ", "").strip()
        if naat in IslamicAudio.islamicAudio:
            talk(f"Playing {naat} on YouTube")
            webbrowser.open(IslamicAudio.islamicAudio[naat])
        else:
            talk(f"Sorry, I don't have {naat} in my library.")
        

    # Get the current time
    elif "what is the time" in command:
        import datetime
        now = datetime.datetime.now()
        talk(f"The time is {now.strftime('%I:%M %p')}")

    # Open a specific file or folder (example for Windows)
    elif "open documents" in command:
        talk("Opening Documents folder")
        os.startfile("C:\\Users\\YourUsername\\Documents")

    # Default response for unknown commands
    else:
        talk("Sorry, I don't understand that command.")

# Main program
if __name__ == "__main__":
    talk("Initializing Sen ...")
    print("Initializing Sen...")

    while True:
        try:
            # Wait for the wake word "Hello"
            print("Listening for wake word...")
            with sp.Microphone() as source:
                
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)  # Adjust timeout and phrase limit as needed

            # Recognize the wake word
            word = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {word}")

            if word == "hello":
                talk("Yes, I am listening.")
                print("Sen activated. Waiting for command...")

                # Listen for the command
                with sp.Microphone() as source:
                    
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

                # Recognize and process the command
                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")
                commandProcess(command)

        except sp.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sp.RequestError:
            print("Sorry, there was an issue with the request.")
        except sp.WaitTimeoutError:
            print("Listening timed out. Please try again.")
        except Exception as e:
            print(f"Error: {e}")