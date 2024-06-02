# voice_recognition.py
import speech_recognition as sr
#from init import recognizer, speak


def listen_for_command():
    with sr.Microphone() as source:
        print("Ecoute...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5) # Ajoutez une limite de temps de 5 secondes
    return audio

def transcribe_audio(audio):
    try:
        prompt = recognizer.recognize_google(audio, language="fr-FR")
        print("Tu as dit: " + prompt)
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
        prompt = None
    except sr.RequestError as e:
        print("Erreur de service; {0}".format(e))
        prompt = None

    if prompt is None:
        return None

    # # Synthétisez la réponse
    # speak("Tu as dit " + prompt)

    return prompt

# chatgpt.py

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

