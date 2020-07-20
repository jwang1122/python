"""
create a new file, and write string to it.
"""
file1 = open("hello.txt", mode="a")
print("Hello, world!", file=file1)
file1.close()
print("Done")