# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (JBernales, 5.15.2023, edited script):
# RRoot,1.1.2030,Created started script
# JBernales,5.15.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None # An object that represents a file
strFile = "ToDoList.txt" # A text file containing user input
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
task = "" # User's task input
priority = "" # User's priority input
taskpriorityline = "" # User's input containing a task with a priority number

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# Get user Input

objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Split() returns a list
    dicRow = {task:lstRow[0], priority:lstRow[1].strip()}  # Convert list to dictionary
    lstTable.append(dicRow)  # Adding dictionary to a table
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("You have selected: Option 1")
        print(lstTable) # Displays the current table with entered user input
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("You have selected: Option 2")
        task = input("What new task would you like to add? ") # Assigns user's task input to the "task" variable
        priority = input("What priority would you rank this task? ") # Assign's user's priority to task
        dicRow = {"Task": task, "Priority": priority} # Displays a row with Task & Priority separated by commas
        lstTable.append(dicRow) # Adds this new row to the list
        for objrow in lstTable:
            print(objrow) # Displays each line entered so far in list
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("You have selected: Option 3")
        print(lstTable)  # Displays each line entered so far in list
        strRemove = input("Enter a task to remove:") # Prompts user to enter task to delete
        for dicRow in lstTable:
            if strRemove.lower() == dicRow["Task"].lower():
                lstTable.remove(dicRow) # Removes task from list if already in list
        print(lstTable)
        input("Task has been removed! Press enter to return to the menu.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("You have selected: Option 4...Saving data to file")
        objFile = open("/Users/janellebernales/Documents/_PythonClass/Assignment05/ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write("{0},{1}\n".format(dicRow["Task"], dicRow["Priority"]))
        objFile.close()
        print("Data saved to file!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("You have selected: Option 5...Exiting program. Goodbye!")
        break  # Exits the program
else:
    print("Please select an option to perform: [1 to 5] - ")