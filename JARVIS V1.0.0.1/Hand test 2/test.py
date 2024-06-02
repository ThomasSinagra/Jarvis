import multiprocessing
import time
import cv2
import mediapipe as mp
from math import *

# Création d'une variable partagée
shared_list = multiprocessing.Array('f', [0.0, 0.0, 0.0])

coordoneex=multiprocessing.Array('f',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
coordoneey=multiprocessing.Array('f', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


# Fonction à exécuter dans le processus secondaire
def worker(coordoneey,coordoneex):
    coordoneey = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    coordoneex = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    # Définir la fonction fonctionok pour traiter les données de localisation des points
    def fonctionok(hand_landmarks):
        for idx, landmark in enumerate(hand_landmarks.landmark):
            global coordoneex, coordoneey
            coordoneex[idx]=round(landmark.x,2)
            coordoneey[idx]=round(landmark.y,2)
    # Initialiser la capture vidéo
    cap = cv2.VideoCapture(0)

    # Initialiser le détecteur de mains de MediaPipe
    hands = mp_hands.Hands()

    # Boucle de traitement des frames
    while True:
        # Lire la frame de la vidéo
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir l'image de BGR à RGB
        image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

        # Traiter l'image pour détecter les mains
        results = hands.process(image)

        # Convertir à nouveau l'image en BGR pour l'affichage
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Si des mains sont détectées, dessiner les landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Appeler la fonction fonctionok avec les données de localisation des points
                fonctionok(hand_landmarks)

        # Afficher l'image
        cv2.imshow('Handtracker', image)

        # Quitter la boucle en appuyant sur la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        None

    # Libérer la capture vidéo et fermer les fenêtres
    cap.release()
    cv2.destroyAllWindows()




#------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Création du processus secondaire
    process = multiprocessing.Process(target=worker, args=(coordoneex,coordoneey,))

    # Démarrage du processus secondaire
    process.start()

    # Attente de la fin du processus secondaire

    # Accès à la variable partagée mise à jour par le processus secondaire
    print("Valeur de la variable partagée dans le processus principal :", coordoneex.value)
    while True :
        time.sleep(0.1)
        print("Valeur de la variable partagée dans le processus principal :", coordoneex.value)

    process.close()