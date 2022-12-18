import csv
from pprint import pprint

with open('csv/sample.csv') as f:
    reader = csv.reader(f)
    reader_list = [row for row in reader]
    pprint(reader_list)
