import cvs
from os import path

if path.exists('memory.cvs'):
    with open('memory.cvs', 'r') as file:
        reader = cvs.reader(file)
        for row in reader:
            print(row)
else:
    with open('memory.cvs', 'w') as file:
        writer = cvs.writer(file)
        writer.writerow([1,2,3])

