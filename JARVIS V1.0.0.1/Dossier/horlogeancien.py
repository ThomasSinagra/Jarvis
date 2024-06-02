import threading
import time
from gtts import gTTS
import os

for i in range(10):
    print()

def minuteurdecompte(listtime):
    time.sleep(listtime[0])
    time.sleep(listtime[0]*60)
    print("TOP")
    tts = gTTS(text="C'est FINI", lang='fr')
    tts.save("salutation.mp3")
    os.system("afplay salutation.mp3")




# Créer et démarrer le thread pour le minuteur
def minuteur(listtime):
    if listtime[1] == 'seconde' or listtime[1] == 'secondes':
        thread = threading.Thread(target=minuteurdecompte, args=((listtime[0],),))  # intervalle d'une minute
    if listtime[1] == 'minutes' or listtime[1] == 'minute':
        thread = threading.Thread(target=minuteurdecompte, args=((listtime[0]*60,),))  # intervalle d'une minute
    thread.daemon = True  # le thread s'exécute en arrière-plan
    thread.start()

minuteur([3,"seconde"])






#        print("Minuteur : ", time.strftime("%H:%M:%S", time.localtime()))
#        print(time.strftime("%S", time.localtime()))
#        print(type(time.strftime("%H:%M:%S", time.localtime())))
#        seconde=int(time.strftime("%S", time.localtime()))
#        print(type(seconde))
#        time.sleep(interval)
#        heuredepart=[int(time.strftime("%H", time.localtime())),int(time.strftime("%M", time.localtime())),int(time.strftime("%S", time.localtime()))]
#        print(heuredepart)



# Le reste du code peut continuer à s'exécuter en même temps que le minuteur
#while True:
#    # Faire d'autres choses...
#    print("Continuer à faire d'autres choses pendant que le minuteur tourne...")
#    time.sleep(10)  # pause de 10 secondes pour l'exemple
