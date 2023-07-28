print("Welcome to DHRUV's file organizer!!!")

import os
import shutil

pathToOrganize = input("Enter a path to a folder to organize :")

if os.path.exists(pathToOrganize):
    # exit(-1)
    try:                  # try-ecept block should follow the if or any other block....
                          # Because directly writing the block gives warning like code is not reachable
        os.mkdir(pathToOrganize + '\Documents')
    except FileExistsError:
        print("Folder exists, not creating...")

    try:  # I gusess try-ecept block should follow the if or any other block....
    #     Because directly writing the block gives warning like code is not reachable
        os.mkdir(pathToOrganize + '\Copied_Images')
    except FileExistsError:
        print("Folder exists, not creating...")

    for entry in os.scandir(pathToOrganize):
        if os.path.isfile(entry):
            file_extension = os.path.splitext(entry.path)[1]
            # print(file_extension)
            if file_extension == ".txt" or file_extension == ".docx":
                # print(file_extension)
                dest = os.path.join(pathToOrganize, "Documents")
                shutil.move(entry, dest)  # Move the file to the destination path
                print(f"Moved {entry.path}")
            elif file_extension == ".pdb":
                os.remove(entry)  # Remove the file
            elif file_extension == ".png" or file_extension == ".jpeg":
                dest = os.path.join(pathToOrganize, "Documents")  # Create a path handler
                shutil.copy(entry, dest)  # Copy the file to the destination path
                print(f"Copied {entry.path}")
            else:  # Handling unsupported formats
                print(f"{file_extension} not supported..")

else:
    print("Path does not exist...")
    exit(-1)

