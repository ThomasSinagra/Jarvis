#import socket

#serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#adresse = ('localhost', 5000)
#serveur_socket.bind(adresse)
#serveur_socket.listen(1)
#print("Le serveur est prêt à recevoir des données...")


import socket

# Créer un socket TCP/IP
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse et au port
serveur_address = ('localhost', 5000)
serveur_socket.bind(serveur_address)

# Écouter les connexions entrantes
serveur_socket.listen(5)

while True:
    # Attendre une connexion
    client_socket, client_address = serveur_socket.accept()

    # Recevoir des données du client
    donnees = client_socket.recv(1024).decode()
    print("Données reçues :", donnees)

    # Envoyer une réponse au client
    reponse = "Message reçu par le serveur."
    client_socket.sendall(reponse.encode())

    # Fermer la connexion avec le client
    client_socket.close()
