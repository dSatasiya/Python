# Lab - 11

print("Welcome to DHRUV's folder analyzer program..")

import os

# print(os.getcwd())

userPath = input("Enter a valid user path to be analyzed : ")

if os.path.exists(userPath):
    # print(os.path.split(userPath))
    # f = open(userPath)
    # print("exists...")
    if os.path.isfile(userPath):
        print(f"{userPath} is not a folder")
        exit(-1)
else:
    print(f"The path \"{userPath}\" does not exist")
    exit(-1)

# if os.path.isdir(userPath):
#     print("It is folder...")
# else:
#     print(f"The path \"{userPath}\" is not a folder")
#     exit(-1)
#

fileSizeLimitStr = input("Enter a file ize in bytes : ")

if not fileSizeLimitStr.isnumeric():
    print("The value is not a number")

fileSizeLimit = int(fileSizeLimitStr)
# print(type(fileSizeLimit))

print(f"Current working directory : {os.getcwd()}")   # This will give the entire path of the current working directory where you are currently
                     # working..

os.chdir(userPath)

print(f"Changed current working directory : {os.getcwd()}")


folderCount = 0
fileCount = 0
fullSize = 0
fileLimitCount = 0

for entry in os.scandir(userPath):
    if entry.is_dir():
        folderCount = folderCount + 1
    elif entry.is_file():
        fileCount = fileCount + 1
        fullSize = fullSize + os.path.getsize(entry)
        if os.path.getsize(entry) > fileSizeLimit:
            fileLimitCount = fileLimitCount + 1

print("Files found in user path : %d" % (fileCount))
print("Folders found in user path  : %d" % (folderCount))
print(f"All files in user path take up : {fullSize} bytes")
print(f"Files in user path that exceeded {fileSizeLimit} : {fileLimitCount}")


