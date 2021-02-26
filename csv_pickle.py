import csv
import pickle
from os import path

if path.exists('memory.cvs'):
    with open('memory.cvs', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
else:
    with open('memory.cvs', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([1,2,3])

