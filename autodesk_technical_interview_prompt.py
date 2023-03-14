"""Imagine you are a librarian and want to develop an inventory management system that 
keeps track of which books are in the library and which ones have been checked out. 

Write a program with the following functionality:

The user can print out a list of each book and its status (“on shelf” or “checked out”) 
The user can add new books to the inventory. The default status of newly added books will be “on shelf”
The user can toggle the status of each book between “on shelf” and “checked out”
The user should interact with the program using the command line interface. Your solution can be in the language of your choosing. 

If you have time, think about what other functionality you might add. Try to implement it for an extra challenge!

We expect this Take Home Assignment to take 2-3 hours. If you complete the required functionality in less time, 
we encourage you to try implementing some other features of your choice. You will have 15-20 minutes to present 
your project and then have 10 minutes to receive feedback from peers on Day One and an Autodesk employee on Day Two."""

# Dictionary data structure to display the name of book and it's status as a {key: value} pair.
# If it was a real inventory and books were already availabile in a file, I'd ideally also
# make an option to either search or add books at the beginning, which would direct the user to
# separate questions.

print("Welcome to your local library inventory!\n")
inventory = {} 

def library_system(status="on shelf"):
    book_name = input("Enter the title of the book and press enter: ")   
    first_status_input = input("Enter the status of the book (e.g. 'on shelf'/'checked out') and press ENTER: ")

    while first_status_input != '' and first_status_input != 'on shelf' and first_status_input != 'checked out':
        first_status_input = input("OOPS! Please check that you've typed out your selection correctly. Enter the status of the book (e.g. 'on shelf'/'checked out') and press ENTER: ")

    if first_status_input != '':    
        status = first_status_input

    inventory[book_name] = status

    add_additional_books_prompt = input("Do you wish to add to OR modify your inventory (y or n)?: ")

    if add_additional_books_prompt == "y":
        library_system()
    else:
        return print(f"Your inventory is: {inventory}")


library_system()
