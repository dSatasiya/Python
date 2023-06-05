# LAB - 6 - Statical Analysis Tool...

print("Welcome to DHRUV's statical analysis tool!")
dataset = [56, 74, -10, 58, 4, 17, 26, 0, 13, 37]
# print(len(dataset))

# use of len() default function to find the lenght of the dataset.
datasetSize = len(dataset)

# Printing the size of the dataset.
print(f"The dataset has {datasetSize} elements")

# Replacing the negative values with zero.
for i in range(datasetSize):
    if dataset[i] <0:
        # print(dataset[i])
        dataset[i] = 0
# print(dataset)

#Sorting of the dataset by .sort() method
dataset.sort()
print(dataset)


# Finding the mean of the dataset...
datasetSum = 0
for val in range(datasetSize):
    datasetSum = datasetSum + dataset[val]

mean = datasetSum/datasetSize
# print(datasetSum)
print(f"The mean of the dataset is = {mean}")

# Calculating the meadian of the dataset.
if datasetSize % 2 != 0:
    medianIndex = int((datasetSize - 1) / 2)
    median = dataset[medianIndex]
    print(f"The median of the dataset = {median}")

else:
    medianIndex1 = int(datasetSize/2) - 1
    medianIndex2 = int(datasetSize/2)
    median = (dataset[medianIndex1] + dataset[medianIndex2]) / 2
    print(f"The median of the dataset = {median}")


# =========================END OF THE CODE===============================
