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

exit_Character = '0'

while(exit_Character != 'q'):

    datafile_path = input("Enter the valid data file path : ")
    if not os.path.exists(datafile_path):
        print("Path does not exist..exiting...")

    else:
        print("\n")
        user_frequency = input("Enter frequency : ")
        user_mode = input("Enter energy mode : ")

        print("\n")
        print(f"{user_mode} power consumption report at {user_frequency} MHz")
        print("     MCU Family |  Power Consumption")
        print("--------------- | --------------------")
        # print("Right path...")
        datafile = open(datafile_path, 'r')
        # for lines in datafile:
        title_line = datafile.readline()
        # print(line)
        column_titles = title_line.split(",")  # .split(",") - here comma means, it is going to
                                            # separate all the items from comma.
        power_cons_list = []
        mcu_list = []
        for data in datafile:
            data_list = data.split(",")
            # print(data_list)

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
            if frequency == user_frequency and energy_mode == user_mode:
                mcu_name = data_list[1]
                # print(mcu_name)
                # calculaitng the power consumption using P = V*I formula...
                power_cons = float(frequency) * float(curr) * float(vdd)
                # print(power_cons)
                power_cons_list.append(power_cons)
                mcu_list.append(mcu_name)
                print("%15s | %.3f uW" % (mcu_name, power_cons))
            else:
                None
        min_power = power_cons_list[0]
        for i in range(0, len(power_cons_list)):
            if power_cons_list[i] < min_power:
                min_power = power_cons_list[i]
                efficient_mcu = mcu_list[i]
            else:
                None
        print(f"Most-efficient MCU in {user_mode} at {user_frequency} mHz : {efficient_mcu}")
    print("\n")
    exit_Character = input("Enter 'q' to exit or 'c' to continue : ")

