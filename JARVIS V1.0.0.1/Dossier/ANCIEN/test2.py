import openai
# from init import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def send_request_to_gpt(prompt, context=None):
    if context:
        prompt = context + prompt

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response["choices"][0]["text"]
    except openai.error.RateLimitError as e:
        print("Error: Rate limit exceeded. Please check your plan and billing details.")
        return "Je suis désolé, je ne peux pas répondre pour le moment. Veuillez réessayer plus tard."
    except Exception as e:
        print("Error: ", e)
        return "Je suis désolé, une erreur est survenue. Veuillez réessayer plus tard."

import speech_recognition as sr
from gtts import gTTS
import os

def skip(n):
    for i in range(n):
        print()

# Création d'un objet Recognizer
recognizer = sr.Recognizer()

def speech(text):
    tts = gTTS(text=text, lang='fr')
    tts.save("salutation.mp3")
    os.system("afplay salutation.mp3")

def respond(text):
    print("\033[0;34mJARVIS :")
    print(text,"\033[0m")
    speech(text)

def transcription(audio):
    try:
        ph=recognizer.recognize_google(audio, language='fr-FR')
        skip(3)
        print("Transcription: " + recognizer.recognize_google(audio, language='fr-FR'))
        return ph
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que tu as dit")
    except sr.RequestError as e:
        print("Erreur lors de la requête vers l'API Google : {0}".format(e))

def listen():
    with sr.Microphone() as source:
        print("Dis quelque chose...")
        audio = recognizer.listen(source) 
        return transcription(audio)



ph=listen()
send_request_to_gpt(ph)
