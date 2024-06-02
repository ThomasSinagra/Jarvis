import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

sentence = "Je veux aller au cinéma."
tokens = word_tokenize(sentence)
print(tokens)
print()


