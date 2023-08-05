# Project - 2 ==> MCU Energy mode analyzer..

import os
import math
print("Welcome to DHRUV's MCU Energy Mode Analyzer")

em0_dataset = {"MCU1": []}
em1_dataset = {"MCU1": []}
em2_dataset = {"MCU1": []}
em3_dataset = {"MCU1": []}
em4_dataset = {"MCU1": []}

all_frequencies: list = []

ENERGY_MODE_0 = "EM0"
ENERGY_MODE_1 = "EM1"
ENERGY_MODE_2 = "EM2"
ENERGY_MODE_3 = "EM3"
ENERGY_MODE_4 = "EM4"

datafile_path = input("Enter the valid datar file path : ")
freq = input("Enter frequency : ")
mode = input("Enter energy mode : ")

print("\n")
print(f"{mode} power consumption report at {freq} MHz")
print("     MCU Family |  Power Consumption")
print("--------------- | --------------------")

if not os.path.exists(datafile_path):
    print("Path does not exist..exiting...")

else:
    # print("Right path...")
    datafile = open(datafile_path, 'r')
    # for lines in datafile:
    title_line = datafile.readline()
    # print(line)
    column_titles = title_line.split(",")  # .split(",") - here comma means, it is going to
                                            # separate all the items from comma.
    # for title in column_titles:
    #     print(title)
    mcu_list = []
    mcu_counter = 0
    for data in datafile:
        # data_line = datafile.readline()
        #converting data into the list....
        data_list = data.split(",")
        # print(data_list)

        #Dividing the MCU families...
        mcu_list.append(data_list[1])
        mcu_counter = mcu_counter + 1

        # frequency access...
        frequency = data_list[3]
        energy_mode = data_list[0]
        # print(frequency)

        #appending all the frequencies into the list....
        all_frequencies.append(frequency)

        # Accessing the current values...
        curr = data_list[4]

        # Accessing the vdd values
        vdd = data_list[5]

        # freq = '12'
        # mode = "EM0"
        # def findMcuFamilies(freq, mode):
        # for val in all_frequencies:
        if frequency == freq and energy_mode == mode:
            mcu_name = data_list[1]
            # print(mcu_name)
            # calculaitng the power consumption using P = V*I formula...
            power_cons = float(frequency) * float(curr) * float(vdd)
            # print(power_cons)
            print("%15s | %.3f uW" % (mcu_name, power_cons))

        # findMcuFamilies(freq, mode)

        #Bifurcating the power consumtion according to the energy mode...
        '''if data_list[0] == ENERGY_MODE_0:
            em0_dataset["MCU1"].append(power_cons)
        elif data_list[0] == ENERGY_MODE_1:
            em1_dataset["MCU1"].append(power_cons)
        elif data_list[0] == ENERGY_MODE_2:
            em2_dataset["MCU1"].append(power_cons)
        elif data_list[0] == ENERGY_MODE_3:
            em3_dataset["MCU1"].append(power_cons)
        elif data_list[0] == ENERGY_MODE_4:
            em4_dataset["MCU1"].append(power_cons)
        # else:
        #     print("Warning : Energy mode EMx is not supported")'''
    # print(em0_dataset)
    # print(em1_dataset)
    # print(em2_dataset)
    # print(em3_dataset)
    # print(em4_dataset)
    #     print(power_cons)
    # print(all_frequencies)

    # print(mcu_family_counter)



