from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

def lemm(m):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    word = m
    lemma = lemmatizer.lemmatize(word)
    stem = stemmer.stem(word)

    print("Lemmatization:", lemma)
    print("Stemming:", stem)

def traitement(ph):
    phl=ph.split(" ")
    phl = [word for word in phl if word != '']
    for i in phl:
        lemm(i)

traitement("Bonjour je suis très grande et je mangerais des pâtes")