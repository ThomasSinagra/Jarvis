import pyautogui
import time

# Déplace la souris à la position (x, y) en 2 secondes
pyautogui.moveTo(400, 400, duration=1)

# Effectue un clic gauche à la position actuelle de la souris
pyautogui.click()

# Attends 1 seconde
time.sleep(1)

# Effectue un double clic gauche à la position actuelle de la souris
pyautogui.doubleClick()

# Attends 1 secoqnde
time.sleep(1)

# Simule l'appui sur la touche "a"
pyautogui.press('a')

# Attends 1 seconde
time.sleep(1)

# Simule l'appui sur les touches "ctrl" + "c" (copier)
pyautogui.hotkey('ctrl', 'c')

# Déplace la souris relativement à sa position actuelle
pyautogui.moveRel(100, 0, duration=1)  # Déplace la souris de 100 pixels vers la droite

# Scrolle vers le bas de 200 pixels
pyautogui.scroll(-200)

# Scrolle vers le haut de 200 pixels
pyautogui.scroll(200)
