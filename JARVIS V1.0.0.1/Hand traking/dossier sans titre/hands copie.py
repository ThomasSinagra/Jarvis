import cv2
import mediapipe as mp
from math import *
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
x4=0
y4=0
x8=0
y8=0
coordoneex=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
coordoneey=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def pythagoras(x4,y4,x8,y8):
    a=abs(x4-x8)
    b=abs(y4-y8)
    c=sqrt((a**2)+(b**2))
    print("DISTANCE POUCE-INDEXE = ",str(round(c,2)))

def fonctionok(hand_landmarks):

    for idx, landmark in enumerate(hand_landmarks.landmark):
        global x4,y4,x8,y8,coordoneex, coordoneey
        coordoneex[idx]=round(landmark.x,2)
        coordoneey[idx]=round(landmark.y,2)
        if idx==4:
            x4=landmark.x
            y4=landmark.y
        if idx==8:
            x8=landmark.x
            y8=landmark.y

        pythagoras(x4,y4,x8,y8)




#----------------------------------------------------------------------------------------

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
