* Write a Python program to count the frequency of words in a file, and print out as dict.

for instance, if the file contains the following contents,

```text
this this this this this this this 
append append append append append 
text. text. text. text. text. 
text.append 
welcome you come back!
```

The expected output should look like:

```
Number of words in the file :
Counter({'this': 7,
         'append': 5,
         'text.': 5,
         'text.append': 1,
         'welcome': 1,
         'you': 1,
         'come': 1,
         'back!': 1})
```