# def tryMatchCase():
'''name = input("Enter the name : ")
match name:
    case "Dhruv":
        print("Hii Dhruv !!")
    case "Smit":
        print("Hii Smit !!")
    case "Dev":
        print("Hii Dev !!")
    case _:                  # this is the way to write default case in python
        print("Name not found ...")'''
def menuSelection():
    choice: str = '0'

    while choice != 'q':
        print("Choose menu from below :")
        print("A. Vada Pav")
        print("B. Bhel")
        print("C. Dabeli")
        print("Or press 'q' to exit..")
        choice = input()
        match choice:
            case 'A':
                print("You have selected Vada Pav..")
            case 'B':
                print("You have selected Bhel..")
            case 'C':
                print("You have selected Dabeli..")
            case 'q':
                print("Exiting...")
            case _:
                print("Invalid choice... Please select from the above Menu..")

menuSelection()
