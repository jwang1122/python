import csv

with open('src/data/students.csv', 'r') as covid_19:
    csv_reader = csv.reader(covid_19)
#    next(csv_reader)
    for line in csv_reader:
        print(line) # return each line as list
#        print(line[0])

with open('src/data/students.csv', 'r') as covid19:
    dictReader = csv.DictReader(covid19)
    for row in dictReader:
        print(row["First name"])

with open('src/data/item.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        print(row)