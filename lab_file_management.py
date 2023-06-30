from os import path
print("Welcome to Dhruv's file search utility...") # printing the initial message

filePath = input("Enter the file path to search: ") # promting the user for the file path

if not path.exists(filePath):   # checking if path exists or not?
    print(f"The file path {filePath} does not exist..exiting")
    exit(-1)

fileToSearch = open(filePath, 'r')
# fileToSearch.read()

wordToFind = input("Enter a single word (no space) to search the file: ")
counter = 0
for line in fileToSearch:
    for word in line.split():
        if word == wordToFind:
            counter = counter + 1
# print(counter)

fileToSearch.close()
fileToWrite = open("log.txt", 'w')
fileToWrite.write(f"{wordToFind} was found in {fileToSearch}: {counter} times")
#fileToWrite.write(f"{word} was found in {fileToSearch}: {counter} times")
print(f"{wordToFind} was found in \"{filePath}\": {counter} times")    #printing the last counter message.
fileToWrite.close()






