# LAB - 5, COMP6060 - Systems Programming

# Importing the random mudule to generate the random numbers..
import random

# Printing the initial message..
print("Welcom to DHRUV's random number generator...")

# Defining the function.
def getValidUserInput(promptString, minimumRangeValue, maximumRangeValue):
    promptString = str(numValues) #Casting of the variable.
    if not  promptString.isnumeric():
        print("Error: invalid value")
    elif int(promptString) < minimumRangeValue or int(promptString) > maximumRangeValue: # Checking the range.
        print("Error: invalid value")
    else:
        for num in range(int(promptString)): # Starting of the for loop.
            randomVal = int(random.random() * 100)  # generating the random values using random function...
            print(f"{num + 1} : {randomVal}")   # printing the randomly generated values.
        exit(-1)  # Exiting the code after successfully generating the random numbers.

# Promting the user continuously.
while True:
    # Promting the user to enter the number between 1 and 50
    numValuesStr = input("Please enter the number of value to generate between 1 and 50: ")
    # Casting the number to integer type...
    numValues = int(numValuesStr)
    #Calling the function.
    getValidUserInput(numValues, 1, 50)

#--------------End of the code-------------------------------
