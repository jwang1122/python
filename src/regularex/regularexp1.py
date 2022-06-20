import re

#Check if the string starts with "The" and ends with "Texas":

txt = "The rain in Texas"
expr1 = "^The.*Texas" # .: any characters
x = re.search(expr1, txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

expr2 = "[a-m]"
x = re.findall(expr2, txt)
print(x)
x = set(x)
print(x)

txt = "That will be 59 dollars"

#Find all digit characters:
expr3='\d'
x = re.findall(expr3, txt)
print(x)
