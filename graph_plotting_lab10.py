from matplotlib import pyplot as plt

print("Welcome to DHRUV's ADC Comparator")

time : list = [1, 3, 5, 7, 9, 11]
adcModule1 = [745, 750, 800, 550, 450, 380]
adcMudulde2 = [780, 785, 854, 415, 400, 310]
actualValues = [750, 790, 845, 423, 380, 267]

plt.title("DHRUV's ADC Module Performance Comparison")
plt.xlabel("Seconds")
plt.ylabel("ADC Resolution")
plt.xlim(1, 12)
plt.ylim(0, 1023)
plt.plot(time, adcModule1, marker = 'D', linestyle = 'dashed', color='green', label='ADC Module 1') # here label means legend labels..
plt.plot(time, adcMudulde2, marker = 's', linestyle = 'dotted', color='blue', label='ADC Moudule 2')
plt.plot(time, actualValues, marker = '.', linestyle = 'solid', color='red', label='Actual Values')
# In upper and below all methods of the plot, the orange colored words are called the properties of the built-in method in Python.
plt.legend(loc = "upper right", shadow=True)
# plt.grid()
plt.show()
