import cv2
import mediapipe as mp
from math import *
import threading



def pythagoras(x4,y4,x8,y8):
    a=abs(x4-x8)
    b=abs(y4-y8)
    c=sqrt((a**2)+(b**2))
    #print("DISTANCE POUCE-INDEXE = ",str(round(c,2)))

def interfacethread():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    x4=0
    y4=0
    x8=0
    y8=0
    coordoneex=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    coordoneey=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    # Définir la fonction fonctionok pour traiter les données de localisation des points
    def fonctionok(hand_landmarks):
        # Ici, tu peux traiter les données de localisation des points
        # Par exemple, tu peux imprimer les coordonnées x, y et z de chaque point

        for idx, landmark in enumerate(hand_landmarks.landmark):
            #print(f"Point {idx}: X={landmark.x}, Y={landmark.y}, Z={landmark.z}")
            global coordoneex, coordoneey
            coordoneex[idx]=round(landmark.x,2)
            coordoneey[idx]=round(landmark.y,2)
            print(coordoneex)
            print(coordoneey)

            #print(str(x4),str(y4),str(x8),str(y8))
            pythagoras(x4,y4,x8,y8)



    cap = cv2.VideoCapture(0)

    hands = mp_hands.Hands()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fonctionok(hand_landmarks)

        cv2.imshow('Handtracker', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        None
    cap.release()
    cv2.destroyAllWindows()



def lancementinterface():
    thread = threading.Thread(target=interfacethread)  # intervalle d'une minute
    thread.daemon = True  # le thread s'exécute en arrière-plan
    thread.start()
    return None

lancementinterface()
while True:
    None