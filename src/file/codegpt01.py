# read csv file each line
"""
1. type in English sentence for the code requist as above
2. ctrl+shift+i
3. generate api code for first time and copy/paste

"""
import csv 

with open('data/students.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file)

    for line in csv_reader: 
        print(line)


# 读取csv文件