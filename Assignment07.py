# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple example of exception handling
#              and pickling (storing data in a binary file)
# ChangeLog: (Who, When, What)
# AYi, 11.29.2022,Created Script
# AYi, 11.30.2022,Edited Script
# AYi, 12.1.2022,Finalized Script
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'ChristmasWishList.dat'
userInput = []
wishList = []
list = []

# Processing/Presentation -------------------------- #

print("""
Option Menu:
1) Read data
2) Add data

[Type 'q' to exit at any time.]
""")

strChoice = str(input("Which option would you like to perform? [1 or 2] - "))
print()

# Option 1 allows users to read data from 'ChristmasWishList.dat'
if (strChoice.strip() == '1'):
    file = open(strFileName, "rb")
    while(True): # Getting all data by iterating pickle.load()
        try:
            list = pickle.load(file)
            wishList.append(list)
        except EOFError:
            break
    file.close()
    for row in wishList: # Printing data
        print(row[0] + ', ' + row[1])

# Option 2 allows users to add data to 'ChristmasWishList.dat'
elif (strChoice.strip() == '2'):
    file = open(strFileName, "ab")
    while(True): # Saving multiple items without restarting the program
        print()
        name = str(input("Enter a Name: "))
        if(name.lower() == "q"):
            break
        item = str(input("Enter an Item: "))
        if (item.lower() == "q"):
            break
        userInput = [name, item]
        pickle.dump(userInput, file)
    file.close()

# Other entries exit the program
elif (strChoice.lower() == 'q'):
    print()
    print("Goodbye!")
    pass

# Random input reminds the users to select from given choices
else:
    print()
    print("Error! " + strChoice + " is not an option.")
    pass


