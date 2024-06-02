import nltk
from nltk.corpus import stopwords

# Téléchargement des stop words pour la langue française
nltk.download('stopwords')

# Affichage de la liste des stop words pour le français
stop_words = stopwords.words('french')
print(stop_words)