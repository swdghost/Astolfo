## DEPENDENCIES
import speech_recognition as sr
from elevenlabs import generate , set_api_key, stream

# EXTENSIONS
from AstolfoExtensions.Alphex import get_response
from AstolfoExtensions.DateTime import date, time
from AstolfoExtensions.IpAddress import get_ip_address
from AstolfoExtensions.stats import get_system_stats
from config import *

def voice_input():
    r = sr.Recognizer()
    
    # Set the microphone as the audio source
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        audio = r.listen(source, timeout =5 , phrase_time_limit= 5)

    # Recognize the speech
    try:
        print("Processing your input...")
        text = r.recognize_google(audio, language='en-in')
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "none"
    except sr.RequestError as e:
        print("Could not request results: {}".format(e))
        return "none"
    return text

def voice_output(response) -> None:
    set_api_key(elevenlabs_api_key)
    audio = generate(
            text= response,
            voice="Charlie",
            model="eleven_multilingual_v2",
            stream=True)
    
    stream(audio)

def remove_punctuations(query):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in query:
            if ele in punc:
                query_ = query.replace(ele, "")
            else:
                query_ = query
        return query_

def chat(query):
        query = query.lower()
        query = remove_punctuations(query)
        if query == "what is your name" or query == "who are you" or query == "your name":
            results = "My name is Astolfo . You can also call me Amaze assistant."
            return results

        elif query == 'who created you' or query == 'who built you' or  query == 'who invented you' or query == 'who discovered you' :
            results = "I was created by Sai Ram and Hari Krishna."
            return results 

        elif "introduce yourself" in query:
            results = "I am Astolfo. A Multi-model Artiicial Intelligence Program built to help you learn about a variety of things since the best I can. 24 hours a day, 7 days a week."
            return results
        elif "ip address" in query:
            results = f"Current System IP address is: {get_ip_address()}"
            return results

        elif "system stats" in query:
            cpu_usage, memory_usage = get_system_stats()
            results = f"CPU usage: {cpu_usage:.2f}% | Memory usage: {memory_usage:.2f}%"
            return results
        
        elif "date" in query:
            results = f"The Current date is : {date()}"
            return results
        elif "time" in query :
            results = f"The Current time is : {time()}"
            return results
        else : 
            results = get_response(query)
            return results
        
        