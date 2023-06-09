# This is the project 1.
# Resistor color coding values.

# below is the dataset for all the values of the color bands
resValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
resMultiplier = [0.01, 0.1, 1, 10, 100, 10000, 10000, 1000000, 1000000, 10000000]
resTolerance = [0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10]
resTempCoeff = [15, 25, 50, 100]

#Printing the welcome message...
print("Welcome to DHRUV's Resistor's value calculator")

def getValidValue(minValue, maxValue):  # Difining the main function to get the valid number of color bands(4-6)
    while True:
        promptSrtring = input("Enter the number of bands or 'q' to quit: ")
        totalBandsStr = promptSrtring
        if totalBandsStr=='q':
            print("Exiting...")
            exit(-1)
        elif not totalBandsStr.isnumeric():
            print("Invalid input")
            continue
        elif int(totalBandsStr)<minValue or int(totalBandsStr)>maxValue:  # checking the range of entered band number
            print("Invalid Input")
            continue
        else:
            # print(totalBands)
            def findResistanceValue(totalBands): # function to find the resistors' digit values
                if totalBands == 4:
                    def findResValues():
                        firstDigitStr = input("Enter the resistance band color 1: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")  # prompting the user for 1st color band
                        secondDigitStr = input("Enter the resistance band color 2: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n") # prompting the user for 2nd color band
                        firstDigit = int(firstDigitStr)
                        firstDigitVal = resValues[firstDigit - 1]
                        secondDigit = int(secondDigitStr)
                        secondDigitVal = resValues[secondDigit - 1]
                        return firstDigitVal, secondDigitVal  # returning the values of the first 2 digits
                    def findMultiplier(): # function to find the multiplier
                        multiplierStr = input("Enter the multiplier's band color number: \n1. silver\n2. gold\n3. black\n4. brown\n5. red\n6. orange\n7. yellow\n8. green\n9. blue\n10. violet\n") #prompting the user for multiplier's color band
                        multiplier = int(multiplierStr)
                        multiplierVal = resMultiplier[multiplier - 1]
                        return multiplierVal  # returning the multiplier's value
                    def findTolerance():  # function to find the tolerance
                        toleranceStr = input("Enter the tolerance color band number: \n1. Grey\n2. violet\n3. blue\n4. green\n5. brown\n6. red\n7. gold\n8. silver\n") #propmting the user for the tolerance color band
                        tolerance = int(toleranceStr)
                        toleranceVal = resTolerance[tolerance-1]
                        return toleranceVal # returning the tolerance value

                    myFirstDigit, mySecondDigit = findResValues()
                    myMultiplier = findMultiplier()
                    myTolerance = findTolerance()
                    print(f"Your final value of resistance is {myFirstDigit}{mySecondDigit} x {myMultiplier} +/-{myTolerance}%")
                    print("OR")
                    resistance = int(myFirstDigit+mySecondDigit) * myMultiplier
                    print(f"{resistance} ohms +/-{myTolerance}%")   # printing the final calculated value of the resistors given with different color band
            # print(firstDigitVal)
                # Repeating the same process if the resistor is with 5 color bands.....
                elif totalBands == 5:
                    def findResValue():
                        firstDigitStr = input("Enter the resistance band color 1: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")
                        secondDigitStr = input("Enter the resistance band color 2: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")
                        thirdDigitStr = input("Enter the resistance band color 3: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")  #Prompting the user for the third band color
                        firstDigit = int(firstDigitStr)
                        firstDigitVal = resValues[firstDigit - 1]
                        secondDigit = int(secondDigitStr)
                        secondDigitVal = resValues[secondDigit - 1]
                        thirdDigit = int(thirdDigitStr)
                        thirdDigitVal = resValues[thirdDigit - 1]
                        return firstDigitVal, secondDigitVal, thirdDigitVal
                    # findResValue()
                    def findMultiplier():
                        multiplierStr = input("Enter the multiplier's band color: \n1. silver\n2. gold\n3. black\n4. brown\n5. red\n6. orange\n7. yellow\n8. green\n9. blue\n10. violet\n")
                        multiplier = int(multiplierStr)
                        multiplierVal = resMultiplier[multiplier - 1]
                        return multiplierVal
                    # findMultiplier()
                    def findTolerance():
                        toleranceStr = input("Enter the tolerance color band number: \n1. Grey\n2. violet\n3. blue\n4. green\n5. brown\n6. red\n7. gold\n8. silver\n")
                        tolerance = int(toleranceStr)
                        toleranceVal = resTolerance[tolerance - 1]
                        return toleranceVal

                    myFirstDigit, mySecondDigit, myThirdDigit = findResValue()
                    myMultiplier = findMultiplier()
                    myTolerance = findTolerance()
                    print(f"Your final value of resistance is {myFirstDigit}{mySecondDigit}{myThirdDigit} x {myMultiplier} +/-{myTolerance}%")
                    print("OR")
                    resistance = int(myFirstDigit + mySecondDigit + myThirdDigit) * myMultiplier
                    print(f"{resistance} ohms +/-{myTolerance}%") # Again printing the final values
                # Again, repeating the same process for the 6 color bands resistor
                elif totalBands == 6:
                    def findResValue():
                        firstDigitStr = input("Enter the resistance band color 1: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")
                        secondDigitStr = input("Enter the resistance band color 2: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")
                        thirdDigitStr = input("Enter the resistance band color 3: \n1. black\n2. brown\n3. red\n4. orange\n5. yellow\n6. green\n7. blue\n8. violet\n9. grey\n10. white\n")
                        firstDigit = int(firstDigitStr)
                        firstDigitVal = resValues[firstDigit - 1]
                        secondDigit = int(secondDigitStr)
                        secondDigitVal = resValues[secondDigit - 1]
                        thirdDigit = int(thirdDigitStr)
                        thirdDigitVal = resValues[thirdDigit - 1]
                        return firstDigitVal, secondDigitVal, thirdDigitVal
                    # findResValue()
                    def findMultiplier():
                        multiplierStr = input("Enter the multiplier's band color: \n1. silver\n2. gold\n3. black\n4. brown\n5. red\n6. orange\n7. yellow\n8. green\n9. blue\n10. violet\n")
                        multiplier = int(multiplierStr)
                        multiplierVal = resMultiplier[multiplier - 1]
                        return multiplierVal
                    # findMultiplier()
                    def findTolerance():
                        toleranceStr = input("Enter the tolerance color band number: \n1. Grey\n2. violet\n3. blue\n4. green\n5. brown\n6. red\n7. gold\n8. silver\n")
                        tolerance = int(toleranceStr)
                        toleranceVal = resTolerance[tolerance - 1]
                        return toleranceVal
                    # findTolerance()
                    def findTempCoefficient():  # function to find the temperature coefficient as there will be last band for the temperature coefficient in the 6 color bands resistor
                        tempCoeffStr = input("Enter the temprature coefficient's band number: \n1. orange\n2. yellow\n3. red\n4. brown\n")
                        tempCoeff = int(tempCoeffStr)
                        tempCoeffVal = resTempCoeff[tempCoeff - 1]
                        return tempCoeffVal # returning the value of temperature coefficient
                    # print(f"Your final value of resistance is {firstDigitVal}{secondDigitVal}{thirdDigitVal} x {multiplierVal} +/-{toleranceVal}% and {tempCoeffVal}ppm temperature coefficient")
                    myFirstDigit, mySecondDigit, myThirdDigit = findResValue()
                    myMultiplier = findMultiplier()
                    myTolerance = findTolerance()
                    myTempCoeff = findTempCoefficient()
                    print(f"Your final value of resistance is {myFirstDigit}{mySecondDigit}{myThirdDigit} x {myMultiplier} +/-{myTolerance}% and temperature coeffiecient is {myTempCoeff}ppm")
                    print("OR")
                    resistance = int(myFirstDigit + mySecondDigit + myThirdDigit) * myMultiplier
                    print(f"{resistance} ohms +/-{myTolerance}% and {myTempCoeff}ppm")  # printing the final value of the function
            totalBands = int(totalBandsStr)
            findResistanceValue(totalBands)
# promptSrtring = input("Enter the number of bands or 'q' to quit: ")
getValidValue(4, 6)   # calling of the main function.



#===============================END OF THE CODE======================================================
