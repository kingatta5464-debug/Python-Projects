import speech_recognition as sr
import webbrowser
import pyttsx3


def processCommand(c):
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    else:
        speak("Sorry Atta, I don’t know that command yet.")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)

            print("Recognizing...")
            word = recognizer.recognize_google(audio).lower()
            print("You said:", word)

            if "jarvis" in word:
                speak("Yes, What do you want me to do?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                command = recognizer.recognize_google(audio).lower()
                print("Command:", command)
                processCommand(command)

            elif "stop" in word or "exit" in word:
                speak("Goodbye Atta!")
                break

        except sr.UnknownValueError:
            print("Could not understand, please try again.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except sr.RequestError:
            print("Network error, please check your connection.")
        except Exception as e:
            print("Error:", e)
