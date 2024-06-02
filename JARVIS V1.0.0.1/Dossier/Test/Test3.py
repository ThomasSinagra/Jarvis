from nltk.stem import PorterStemmer

def stemme(m):
    stemmer = PorterStemmer()
    word = m
    stem = stemmer.stem(word)
    print("Stemming:", stem)


def traitement(ph):
    phl=ph.split(" ")
    phl = [word for word in phl if word != '']
    for i in phl:
        stemme(i)

traitement("Bonjour je suis très grande et je mangerais des pâtes")