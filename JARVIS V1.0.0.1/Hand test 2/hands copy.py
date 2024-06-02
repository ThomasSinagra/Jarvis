import cv2
import mediapipe as mp
import socket

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Créer un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
serveur_address = ('localhost', 5000)
client_socket.connect(serveur_address)

# Définir la fonction fonctionok pour traiter les données de localisation des points
def fonctionok(hand_landmarks):
    coordoneex = []
    coordoneey = []

    for idx, landmark in enumerate(hand_landmarks.landmark):
        coordoneex.append(round(landmark.x, 2))
        coordoneey.append(round(landmark.y, 2))

    # Envoyer les données au serveur
    donnees = "Coordonnées X : " + str(coordoneex) + ", Coordonnées Y : " + str(coordoneey)
    client_socket.sendall(donnees.encode())

# Initialiser la capture vidéo
cap = cv2.VideoCapture(0)

# Initialiser le détecteur de mains de MediaPipe
hands = mp_hands.Hands()

# Boucle de traitement des frames
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

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
client_socket.close()
