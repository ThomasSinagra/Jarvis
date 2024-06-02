import csv
import os
from gtts import gTTS
import pyperclip
import csv


from JARVISLIB_horloge import *


#Initialisation et récupération des listes :

with open('stopword.csv', 'r') as file:
    reader = csv.reader(file)
    stopwords = next(reader)

#-----------------------------------------------------------------------------------------------------------------------
#Analyse
