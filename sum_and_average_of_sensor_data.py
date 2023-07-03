import os

myFile = open('sensor_data.txt', 'r')
mySum : float = 0
sampleCnt : int = 0
for line in myFile:
    # print(line)
    lineList : list = []
    lineList = line.split()
    # print(lineList)
    # updatedList : list = []
    lineList.pop(0)   # .pop() and .insert() methods are used to delete and insert the item with location.
    # updatedList.append(lineList)
    # print(lineList)
    square : float = 0
    square = float(lineList[1]) ** 2
    lineList.insert(2, str(square))
    sampleCnt = sampleCnt + 1
    mySum = mySum + float(lineList[2])
    print(lineList)

myAverage : float = 0
myAverage = mySum / sampleCnt
# print(mySum)
# print(sampleCnt)
# print(myAverage)
print(f"\n\nThe sum of total {sampleCnt} samples is {mySum} and \nThe average of all the samples is {myAverage}")
print("_______________Here are the rounded values of the same______________")
print("The sum is : %.4f \nThe average is : %.4f" %(mySum, myAverage))
print("Complete !!!")
