import math

print("Welcome to DHRUV's number analyzer !")

dataSet = { 'radii' : [5.5, 6.3],
            'angles' : [56, 180, 320, 15, 90]
           }
# print(dataSet)

print("Select the set of numbers to analyze: ")
counter : int = 1;
# print(len(dataSet))
for key in dataSet.keys():
    print(f"{counter}: {key}")
    counter = counter + 1

keyNum = input()
# print(keyNum)

# Calculating Circle and Sphere Area....
if int(keyNum) == 1:
    for radius in dataSet['radii']:
        # print(radius)
        area = math.pi * radius * radius
        sphereVol = 4/3 * math.pi * (radius ** 3)
        print(f"{radius} radius circle area = %.3f " %(area))
        print(f"{radius} radius sphere volume = %.3f " % (sphereVol))
        print("\n")

# Calculating  the sine and cosine angles..........
elif int(keyNum) == 2:
    for angle in dataSet['angles']:
        sinValue = math.sin(angle)
        cosValue = math.cos(angle)
        print(f"{angle}° sin = %.2f" %(sinValue))
        print(f"{angle}° cosine = %.2f" %(cosValue))
        print("\n")

else:
    print("Invalid number... exiting")

