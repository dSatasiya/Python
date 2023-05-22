# printing the initial message.....
print("Welcome to DHRUV's GPA Calculator")
marks = input("Please enter your grade from 100: ")
# prompting the user for the grade percentage...
def getValidUserInput(promptStirng, minimumRangeValue, maximumRangeValue):
    # promptStirng = int(input(("Enter the marks to get the GPA :")))
    if not promptStirng.isnumeric(): # Checking whether input is numeric or any name with characters..
        print("Value entered was not a number. Exiting....")
        exit(-1)
    else:
        promptInt = int(promptStirng)
        if promptInt < minimumRangeValue or promptInt > maximumRangeValue: # Checking for the range
            print("The number entered is out of the range....")
        elif promptInt>=90 and promptInt<=100:
            print("Your GPA is 4.2")
        elif promptInt>=80 and promptInt<=89:
            print("Your GPA is 4.0")
        elif promptInt>=75 and promptInt<=79:
            print("Your GPA is 3.5")
        elif promptInt>=70 and promptInt<=74:
            print("Your GPA is 3.0")
        elif promptInt>=65 and promptInt<=69:
            print("Your GPA is 2.5")
        elif promptInt>=60 and promptInt<=64:
            print("Your GPA is 2.0")
        elif promptInt>=55 and promptInt<=59:
            print("Your GPA is 1.5")
        elif promptInt>=50 and promptInt<=54:
            print("Your GPA is 1.0")
        else:
            print("FAIL")

getValidUserInput(marks, 0, 100) #Calling the getValidUserInput

