import cv2
import mediapipe as mp
from math import *
import threading
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

coordoneex=[1,1,1,10,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
coordoneey=[1,1,1,10,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

class button:
    def __init__(self, marque, couleur, vitesse):
        self.posx = marque
        self.posy = couleur
        self.vitesse = vitesse

    def accelerer(self, increment):
        self.vitesse += increment

    def freiner(self, decrement):
        self.vitesse -= decrement

def pythagoras(x4,y4,x8,y8):
    a=abs(x4-x8)
    b=abs(y4-y8)
    c=sqrt((a**2)+(b**2))
    return c

def fonctionok(hand_landmarks):

    for idx, landmark in enumerate(hand_landmarks.landmark):
        global coordoneex, coordoneey
        coordoneex[idx]=round(landmark.x,2)
        coordoneey[idx]=round(landmark.y,2)




#----------------------------------------------------------------------------------------
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




    if pythagoras(coordoneex[8],coordoneey[8],coordoneex[4],coordoneey[4])<0.05:
        for i in range(10):print()
        print("CLICK-------------------------------")
    else:
        for i in range(10):print()
        print("no click")
    #print(round(pythagoras(coordoneex[8],coordoneey[8],coordoneex[4],coordoneey[4]),2))


# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
