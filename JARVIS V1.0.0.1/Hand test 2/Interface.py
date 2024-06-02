import tkinter as tk

def on_button_click():
    label.config(text="Bouton cliqué !")


# Création de la fenêtre principale
root = tk.Tk()
root.title("JARVIS INTERFACE")
root.iconbitmap('JARVIS.ico')  # Remplace "chemin_vers_ton_icone.ico" par le chemin de ton fichier .ico


def change_label_text():
    label.config(text="Nouveau texte du label")

# Création d'un label
label = tk.Label(root, text="Cliquez sur le bouton")
label.place(x=10, y=100)

# Création d'un bouton
button = tk.Button(root, text="Cliquez ici", command=change_label_text)
button.place(x=150, y=100)  # Placement du bouton à x=150, y=100

# Boucle principale pour afficher la fenêtre
root.mainloop()
