import colorama
from colorama import Fore, Back, Style
print(Fore.RED + "Hello World")
print(Fore.GREEN + "Dhruv Satasiya")
# print(Back.CYAN + "Dhruv Satasiya")
print(Fore.RED + "Dhruv Satasiya")
print("Hii")
print(Style.RESET_ALL)
print("Hii")
sum = 10
print(f"This is the sum : {Fore.CYAN + str(sum)}")
print(Style.RESET_ALL)
# print("This is Black Fonts")

# Output:
Hello World      # red colored
Dhruv Satasiya   # green colored
Dhruv Satasiya   # red colored
Hii

Hii
This is the sum : 10
