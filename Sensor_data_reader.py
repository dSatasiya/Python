# This is lab - 8
print("Welcome to DHRUV’s sensor data reader!")

tempSum = 0
tempNum = 0
humidSum = 0
humidNum = 0

file = open("sensor_data.txt", "r")

for i in file:
    line = i.split()
    # print(line)
    for word in line:
        # print(word)

        if word == "Temp":
            tempNum = tempNum+ 1
            tempSum = float(line[2]) + float(tempSum)

        elif word == "Humid":
            humidNum = humidNum+ 1
            humidSum = float(line[2]) + float(humidSum)

file.close()
tempAvg= tempSum/tempNum
humidAvg= humidSum/humidNum
print(f"{'Temperature Average '}", end= "|" f"{' Humid Average'}\n")
print(f"{tempAvg:10.3f}\t\t\t| {humidAvg:10.3f}")

