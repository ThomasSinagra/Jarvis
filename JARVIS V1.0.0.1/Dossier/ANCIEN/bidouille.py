import threading
import time

def minuteur(interval):
    while True:
        print("Minuteur : ", time.strftime("%H:%M:%S", time.localtime()))
        time.sleep(interval)

# Créer et démarrer le thread pour le minuteur
thread = threading.Thread(target=minuteur, args=(6,))  # intervalle d'une minute
thread.start()

# Le reste du code peut continuer à s'exécuter en même temps que le minuteur
while True:
    # Faire d'autres choses...
    print("Continuer à faire d'autres choses pendant que le minuteur tourne...")
    time.sleep(10)  # pause de 10 secondes pour l'exemple


