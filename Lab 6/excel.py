import csv

with open('test.csv') as f:
    data = csv.reader(f)
    for i in data:
        print(i)

