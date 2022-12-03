# Pickling with Exception Handling
## Introduction
Pickling is a method to save in and read from a binary file. In this assignment, pickle.load() and pickle.dump() were used to learn about how pickling process works.

## Setup
```
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
```
Similar to previous assignments, I wanted to set up options in my program to explore different functions.

## Option 1: Allow users to read data from .dat file
```
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
```
Here, try/except statement had to be used to retrieve all data through pickle.load() function because the program does not know when to stop the while loop. The try/except allowed the program to only run until all of the data is retrieved from .dat file. 

The following screenshot shows the error when try/except statement is not used:
 
This type of error handling is further explained in GeeksforGeeks’s article called Handling EOFERROR exception in Python.
Also, the file.close() function was used outside the while loop because otherwise, the program would have repeatedly read the first line. Then every row was stored in wishList.

## Option 2: allow users to add data to .dat file
```
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
```
This part of the script was written for the user input to be automatically saved in .dat file. This allows for each item to be saved as one element and can be retrieve as such.

## Other options
```
elif (strChoice.lower() == 'q'):
    print()
    print("Goodbye!")
    pass

else:
    print()
    print("Error! " + strChoice + " is not an option.")
    pass
```
The rest of the script was similar to ones used in previous assignments. The ‘Q’ option allows for users to exit the program, while any other input notifies users that they need to type options that are given. Here pass was used instead of break because loop was not used.
Conclusion
There were a lot challenges I encountered while trying to use pickle functions (load and dump) within classes and definitions. In the future, with more time, I would like to explore options utilizing loops and functions similar to Assignment 6.


Works Cited
Dawson, M. (2010). Python programming for the absolute beginner: Michael Dawson. Course Technology Cengage Learning. 
Handling EOFERROR exception in Python. GeeksforGeeks. (2020, September 2). Retrieved November 30, 2022, from https://www.geeksforgeeks.org/handling-eoferror-exception-in-python/ 
Root, Randal. _Mod7PythonProgrammingNotes. Microsoft Docs. Retrieved November 29, 2022.


