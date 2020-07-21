import csv

with open('./data/data_minimal.csv', 'r') as covid_19:
    csv_reader = csv.reader(covid_19)
#    next(csv_reader)
    count = 0
    for line in csv_reader:
        print(line) # return each line as list
        print(line[0])
        count += 1
        if count > 10:
            break

with open('students.csv', 'r') as student:
    dictReader = csv.DictReader(student)
    for row in dictReader:
        print(row)
        id = row.get("ID")
        print(id)
        first = row["First name"]
        print(first)