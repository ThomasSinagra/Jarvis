import multiprocessing

import cv2
import mediapipe as mp
from math import *
from multiprocessing import Process




def pythagoras(x4, y4, x8, y8):
    a = abs(x4 - x8)
    b = abs(y4 - y8)
    c = sqrt((a ** 2) + (b ** 2))
    #print("DISTANCE POUCE-INDEXE = ", str(round(c, 2)))

def fonctionok(hand_landmarks):
    coordoneex = [round(landmark.x, 2) for landmark in hand_landmarks.landmark]
    coordoneey = [round(landmark.y, 2) for landmark in hand_landmarks.landmark]
    print(coordoneex)
    print(coordoneey)
    #print(str(x4), str(y4), str(x8), str(y8))
    #pythagoras(x4, y4, x8, y8)

def interfacethread():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
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

    cap.release()
    cv2.destroyAllWindows()

def lancementinterface():
    p = Process(target=interfacethread)
    p.start()
    p.join()

if __name__ == '__main__':
    lancementinterface()
    freezesupport()