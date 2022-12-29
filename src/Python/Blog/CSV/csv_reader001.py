import csv

with open('csv/sample.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
