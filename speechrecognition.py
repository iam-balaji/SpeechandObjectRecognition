import speech_recognition as sr
import time
import random
import datetime
import os
from wikipedia import wikipedia
from gtts import gTTS
from googlesearch import search

import warnings

recogniser = sr.Recognizer()
data_list = []

warnings.filterwarnings('ignore')


#Function to Listen to the audio
def recordAudio():
    with sr.Microphone() as audio_source:
        print("I am listening, Speak into the microphone")
        audio = recogniser.listen(audio_source)
        speechtotext = recogniser.recognize_google(audio)
        return speechtotext
   
       





#Greet User with a phrase 
def greetings(speechtotext):
     greeting_words=['hey','hello','hi']
     greeting_response = ['hey there','hello','whatsup']
    #  speechtotext = speechtotext.lower()
     for input in speechtotext.split():
         if input.lower() in greeting_words:
             return random.choice(greeting_response)
         else:
                return ''



#Function to check Wakeword
def wakeAssistant (speechtotext):
    wakeWord = ['hey jarvis' , 'alexa']
    speechtotext = speechtotext.lower()
    for words in wakeWord:
        if words in speechtotext:
            return True
        else:
            return False

# Function to get the virtual assistant response
def assistanceResponse(response):
        assobj = gTTS(text=response,lang='en',slow = False)
        assobj.save('reply.mp3')
        os.system('start reply.mp3')
        time.sleep(10)

  #Function to split the person's name from the sentence  
def getPersonDetails(speechtotext):
    words = speechtotext.split()

    for word in range(0,len(words)):
        if word+3<=len(words)-1 and words[word].lower() == 'who' and words[word+1].lower() =='is':
            return words[word+2] and words[word+3]
    


if __name__ == "__main__":
    while True:
        speechtotext = recordAudio()
        response = ""
        if wakeAssistant(speechtotext) == True:
            response = response + greetings(speechtotext)

            if 'date' in speechtotext:
                    dateTime = datetime.datetime.now()
                    print(dateTime.strftime("%x"))
                    response = response + "The date is {}".format(dateTime)

            if 'time' in speechtotext:
                    dateTime = datetime.datetime.now()
                    value = dateTime.replace(second=0,microsecond=0)
                    response =  response + ""+"The time is {}" .format(value)

            # To check whether user said 'Who is'
            if 'who is' in speechtotext:
                        personDetails =  getPersonDetails(speechtotext)
                        wiki = wikipedia.summary(personDetails , sentences=1,auto_suggest=True)
                        response = response+"  "+ wiki
        
        assistanceResponse (response)