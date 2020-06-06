import speech_recognition as sr
import time
from googlesearch import search
recogniser = sr.Recognizer()
data_list = []
def recognition():

    with sr.Microphone() as audio_source:
        print("I am listening, Speak into the microphone")
        audio = recogniser.listen(audio_source)
        speechtotext = recogniser.recognize_google(audio)
        speech(speechtotext)
def speech(data):    
    try:
        print("Please Wait , Searching for your query in the internet")
        query = data
        for text in search(query,tld = "com",lang='en',num=10,stop=10,pause=2.0):
            data_list.append(text)
            print(data_list)
    except:
        print('I did not understand it')
        time.sleep(2) 
        recognition()

if __name__ == "__main__":
    recognition()