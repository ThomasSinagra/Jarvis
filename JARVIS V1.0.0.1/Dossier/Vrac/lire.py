import csv

# Lecture depuis un fichier CSV
with open('stopword.csv', 'r') as file:
    reader = csv.reader(file)
    loaded_list = next(reader)


print(loaded_list) 
