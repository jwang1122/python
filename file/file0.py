"""
create a new file, and write string to it.
"""
oceans = ('Pacific','Atlantic','Indian','Southern','Arctic')

file1 = open("hello.txt", "+w")
print("Hello, world!", file=file1)

name = input("Enter your name please: ")
print(f"Hello {name}.", file=file1)

for ocean in oceans:
    file1.write(ocean)
    file1.write("\n")

file1.close()
print("Done")
