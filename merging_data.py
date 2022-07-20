import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'brown_dwarfs.csv'

df1 = []
df2 = []

with open(file1, 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        df1.append(i)

with open(file2, 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        df2.append(i)

h1 = df1[0]
h2 = df2[0]

data1 = df1[1:]
data2 = df2[1:]

h = h1 + h2

data = []

for i in data1:
    data.append(i)

for i in data2:
    data.append(i)

with open('total_stars.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(data)

df = pd.read_csv('total_stars.csv')
df.tail(8)