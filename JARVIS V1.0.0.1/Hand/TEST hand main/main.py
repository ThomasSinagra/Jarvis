import speech_recognition as sr
from gtts import gTTS
import os
import time
import csv
import pyperclip
from JARVISLIB_notification import *
from JARVISLIB_horloge import *
import JARVISLIB_openapp
import JARVISLIB_createfile

import multiprocessing

import multiprocessing

if __name__ == '__main__':
    # Spécifier la méthode de démarrage de processus à utiliser
    multiprocessing.set_start_method('spawn')
    print("a")
    # Importer et appeler la fonction lancementinterface() depuis newhand
    import newhand
    newhand.lancementinterface()




systeme="MacOS"
if __name__ == '__main__':
    newhand.lancementinterface()
# initialisation

with open('stopword.csv', 'r') as file:
    reader = csv.reader(file)
    stopwords = next(reader)

# Création d'un objet Recognizer
recognizer = sr.Recognizer()

for i in range(10):print()

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
        for i in range(3):print()
        print("Transcription: " + recognizer.recognize_google(audio, language='fr-FR'))
        return ph
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que tu as dit")
        return []
    except sr.RequestError as e:
        print("Erreur lors de la requête vers l'API Google : {0}".format(e))
        return []

def listen():
    with sr.Microphone() as source:
        print("Dis quelque chose...")
        audio = recognizer.listen(source) 
        return transcription(audio)



#-------------------------------------



def speech(text):
    tts = gTTS(text=text, lang='fr')
    tts.save("salutation.mp3")
    os.system("afplay salutation.mp3")

def respond(text):
    print("\033[0;34mJARVIS :")
    print(text,"\033[0m")
    speech(text)
def tokenisation(text):
    phlc=text.split(" ")
    return phlc

def deletespacejarvis(list):
    phl = [word for word in list if word != '' and word != 'jarvis' and word != '.']
    return phl

def delstopword(list):
    phls = [word for word in list if word not in stopwords]
    return phls

def traitement(text):
    phlc=tokenisation(text)
    phl=deletespacejarvis(phlc)
    phls=delstopword(phl)

    print("phlc : ",phlc)
    print("phl : ",phl)
    print("phls : ",phls)

    return(phls)

def interpretation(text):
    phls = traitement(text)
    phlc=tokenisation(text)
    while phls and phls[0] != "Jarvis":
        del phls[0]
    print("Phrase simplifié liste : ",phls)
    if len(phls)!=0:
        if phls[0]=="Jarvis":
            if "minuteur" in phls:
                phlstemp=phls
                for i in phlstemp:
                    try:
                        chiffre=int(i)
                    except:
                        None
                    else:
                        try:
                            if phlstemp[(phlstemp.index(str(i)))+1]=="seconde" or phlstemp[(phlstemp.index(str(i)))+1]=="secondes":
                                temps=chiffre
                            if phlstemp[(phlstemp.index(str(i)))+1]=="minute" or phlstemp[(phlstemp.index(str(i)))+1]=="minutes":
                                temps=chiffre*60
                            if phlstemp[(phlstemp.index(str(i)))+1]=="heure" or phlstemp[(phlstemp.index(str(i)))+1]=="heures":
                                temps=chiffre*3600
                                print("TEMPS =====", temps)
                        except:
                            None
                        else:
                            print("temps = ",temps)
                            respond(("Lancement du minuteur de "+ str(chiffre) +" "+ phlstemp[(phlstemp.index(str(i)))+1]))
                            lancementminuteur(temps)
            if "enregistre" in phls and "copié" in phls:
                print("ok je copier")
                spam = [pyperclip.paste()]
                #
                respond("C'est copié, quel nom est a donner au fichier de sauvegarde ?")
                ph=listen()
                print(ph)
                namefile=(ph+".csv")
                respond(("Ok, ce fichier s'appele donc "+namefile))
                #
                with open(namefile, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(spam)
            if "copie" in phls and "adresse" in phls:
                print("Ok")
                try:
                    if phls[(phls.index('adresse')+1)]=="mail":
                        pyperclip.copy("thomas.sinagra.08@gmail.com")
                except:
                    None
            if "ouvre" in phls:
                if "Minecraft" in phls:
                    JARVISLIB_openapp.openapp('Minecraft')
                elif "discorde" in phls:
                    JARVISLIB_openapp.openapp('Discord')
            if "créer" in phls and "fichier" in phls:
                if "python" in phls:
                    print("sto")
            if "allume" in phls and "l'interface" in phls:
                respond("Ok, je lance l'IHM")

        print()


#-------------------------------------


if systeme=="MacOS":
    sendnotification("Hi it\'s JARVIS, App successfully launched 🥳")

while True :
    ph=listen()
    print(ph)
    if ph!=[]:
        reponse=interpretation(ph)
        if reponse!=None:
            respond(reponse)
            ph=listen()




#------------------------------------------------------------------------------------------------------------------------
#Ancien
#if ph=="Jarvis tu vas bien":
#    respond("Bonjour,je vais bien, comment puis-je vous aider ?")
#    ph=listen()
#    if ph=="ça ira merci":
#        respond("D'accord, dites moi si vous avez besoin de moi")
