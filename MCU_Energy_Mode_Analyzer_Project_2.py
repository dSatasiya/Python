# Project - 2 ==> MCU Energy mode analyzer..

import os
import math
import numpy as np
from matplotlib import pyplot as plt

print("Welcome to DHRUV's MCU Energy Mode Analyzer")

em0_dataset = {}
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
        # print("\n")
        # print("1: 12\n2: 17\n3: 2.4\n4: 21\n5: 25\n6: 3.5\n7: 32\n8: 36")

        user_mode = input("Choose an energy mode (0-4) to analyze : ")
        while(int(user_mode)<0 or int(user_mode)>4):
            print("Error: invalid value, please try again...")
            user_mode = input("Choose an energy mode (0-4) to analyze : ")
            if not user_mode.isnumeric():
                print(f"{user_mode} is not a number. Please try again..")
                user_mode = input("Choose an energy mode (0-4) to analyze : ")
        # elif not user_mode.isnumeric():
        #     print(f"{user_mode} is not a number. Please try again...")
        # else:
        #     None

        if user_mode == '0':
            user_mode = ENERGY_MODE_0
        elif user_mode == '1':
            user_mode = ENERGY_MODE_1
        elif user_mode == '2':
            user_mode = ENERGY_MODE_2
        elif user_mode == '3':
            user_mode = ENERGY_MODE_3
        elif user_mode == '4':
            user_mode = ENERGY_MODE_4

        print("Choose a clock frequency to analyze : ")

        datafile = open(datafile_path, 'r')
        for data in datafile:
            data_list = data.split(",")
            # print(data_list)

            # frequency access...
            frequency = data_list[3]
            energy_mode = data_list[0]
            # print(frequency)

            # appending all the frequencies into the list....
            all_frequencies.append(frequency)

        uni_frequencies = []
        uni_frequencies = np.unique(all_frequencies)
            # print(uni_frequencies)
        frequency_dict = {}
        for i in range(1, len(uni_frequencies)):
            frequency_dict[i] = (uni_frequencies[i])

        for key, value in frequency_dict.items():
            print(f"{key}: {value}")
        datafile.close()

        user_frequency = input()

        print("\n")
        print(f"{user_mode} power consumption report at {frequency_dict[int(user_frequency)]} MHz")
        print("     MCU Family |  Power Consumption")
        print("--------------- | --------------------")

        # print("Right path...")

        def mainFunc():
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
                if frequency == frequency_dict[int(user_frequency)] and energy_mode == user_mode:
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
            print(f"Most-efficient MCU in {user_mode} at {frequency_dict[int(user_frequency)]} mHz : {efficient_mcu}")
            # print(all_frequencies)
            datafile.close()

            print(mcu_list)
            # datafile = open(datafile_path, 'r')

            def powerConsumotionPlot():
                plot_power_cons_list = []
                plot_frequency_list = []
                # my_dict = {}
                for i in range(0, len(mcu_list)):
                    em0_dataset[mcu_list[i]] = []
                    datafile = open(datafile_path, 'r')
                    for plot_data in datafile:
                        list = plot_data.split(",")
                        if mcu_list[i] == list[1] and user_mode == list[0]:
                            plot_power_cons = float(list[3]) * float(list[4]) * float(list[5])
                            # plot_power_cons_list.append(plot_power_cons)
                            em0_dataset[mcu_list[i]].append(plot_power_cons)
                            plot_frequency_list.append(list[3])
                    # print(f"power consumption list for {mcu_list[i]} is {plot_power_cons_list}")
                    # print(f"frequency list for {mcu_list[i]} is {plot_frequency_list}")
                    datafile.close()

                # print(em0_dataset)
                # print(em0_dataset[mcu_list[0]])
                # print(plot_frequency_list)
                plf = np.unique(plot_frequency_list)
                # plf.sort()
                # print(plf)
                # print(plot_power_cons_list)
                plt.xlabel("Clock Frequency (MHz)")
                plt.ylabel("Power Consumption (uW)")
                plt.title(f"{user_mode} Power Consumption Plot")
                for i in range(0, len(mcu_list)):
                    plt.plot(plf, em0_dataset[mcu_list[i]], marker='.')
                plt.legend(em0_dataset.keys())
                plt.show()
                # plt.savefig("F:\Fanshawe Sem-2\COMM-6060-Systems Programming-Python\Project_2/power-consumption.pdf")
                print(f"Plot saved to Project 2 \\{user_mode}-PowerConsumption.pdf. Close Plot Window to Continue...")
            powerConsumotionPlot()
        mainFunc()


    print("\n")
    exit_Character = input("Enter 'q' to exit or 'c' to continue : ")

