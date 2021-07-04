"""
Read csv file.
"""
import pandas as pd

students = pd.read_csv("src/data/students.csv")
print(students)