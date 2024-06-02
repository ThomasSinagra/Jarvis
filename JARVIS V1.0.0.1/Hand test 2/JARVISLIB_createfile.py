import csv

my_list = []

def createfile(type):
    if type=="python":
        with open('pythonfiletest.py', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(my_list)
    if type=="python":
        with open('pythonfile@.py', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(my_list)