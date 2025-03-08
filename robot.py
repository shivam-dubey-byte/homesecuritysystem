import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
from bs4 import BeautifulSoup
import requests
import time
from deepface import DeepFace
import cv2

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice (0 for male, 1 for female)

def image():
    import cv2
    # Initialize the webcam (0 is usually the default camera)
    camera = cv2.VideoCapture(0)
    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Could not open webcam")
        exit()
    # Read a frame from the camera
    ret, frame = camera.read()
    # If a frame is captured successfully
    if ret:
        # Save the image to the current directory
        cv2.imwrite("captured_image.jpg", frame)
        print("Photo taken and saved as captured_image.jpg")
    else:
        print("Failed to capture image")
    # Release the camera
    camera.release()
    # Close any OpenCV windows (not strictly needed here, but a good habit)
    cv2.destroyAllWindows()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wish_me():
    speak("Hi, I'm Chitti the Robot. Speed 1 terahertz, memory 1 zigabyte")
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def google_search(query):
    # Placeholder Google search function; add actual code if needed
    print(f"Searching Google for: {query}")
    return ["Sample result 1", "Sample result 2"]

def run():
    wish_me()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("What do you want to play on YouTube?")
            text = take_command()
            pywhatkit.playonyt(text)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'path_to_your_music_directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "path_to_your_code_editor"
            os.startfile(codePath)
        elif 'search google' in query:
            speak("What do you want to search for?")
            search_query = take_command()
            speak(f"Searching Google for {search_query}")
            search_results = google_search(search_query)
            for result in search_results:
                speak(result)
        elif 'close' in query:
            return 0

def match_face():
    # Compare two images
    result = DeepFace.verify('student1.jpg', 'student2.jpg', enforce_detection=False)
    if result['verified']:
        print("Faces match!")
        return 1
    else:
        print("Faces do not match.")
        return 0

if __name__ == "__main__":
    while True:
        print("Chitti activated")
        check = match_face()
        if check == 1:
            speak('Chitti is activated')
            run()
        else:
            speak("Chitti is Shutting down")
            break
