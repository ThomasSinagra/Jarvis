import threading
import time
from gtts import gTTS
import os

for i in range(3):
    print()



def minuteur(interval):
    print("jbfkjzbfiziudbuf")
    time.sleep(interval)
    tts = gTTS(text="C'est FINI", lang='fr')
    tts.save("salutation.mp3")
    os.system("afplay salutation.mp3")
    return None


def lancementminuteur(temps):
    thread = threading.Thread(target=minuteur, args=(temps,))  # intervalle d'une minute
    thread.daemon = True  # le thread s'exécute en arrière-plan
    thread.start()
    return None



