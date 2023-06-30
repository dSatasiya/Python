# This is the file management in the Python....

import os     # OS library is used for the file management, operating systems and paths in the Python
from os import path

myPath = "F:\Fanshawe Sem-2\COMM-6060-Systems Programming-Python\LABS\Labs/file_management.txt"

# print(myPath)
# myPath = "F:\Fanshawe Sem-2\COMM-6060-Systems Programming-Python\LABS\Labs\file_manage.txt"
# print(myPath)

myFile = open(myPath, 'r')
# print(myFile.read())
# print("\n\n")
print(myFile.read(5))
# print(myFile.readline())
# print(myFile.readlines())
# print(myFile.readlines(3))
# print(myFile.readlines())
# myFile.close()
# myFile = open(myPath, 'w')
# myFile.write("This is the third message")
# myFile.close()
# myFile = open(myPath, 'a')
# myFile.write("\nThis is the fourth message")

searchWord : str = input("Enter the word that you want to search: ")
counter : int = 0
# stringList = []
for line in myFile:
    stringList = line.split()
    # print(stringList)
    for word in stringList:
        if word == searchWord:
            counter = counter + 1

print(counter)
# while True:
# line = myFile.readline()
# print(line)
# for word in line:
#     print(word)

    # print(line.split())
    # print(stringList)

# myString = "My full name is Dhruv Harshadbhai Satasiya"
# print(myString.split())
