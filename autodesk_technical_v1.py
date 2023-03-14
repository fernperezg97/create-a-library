

print("Welcome to your local library inventory!")
inventory = {}
book_name = ''
status = ''

def library_system():
    book_name = input("Enter the title of the book and press enter: ")   
    first_status_input = input("Enter the status of the book (e.g. 'on shelf'/'checked out') and press ENTER: ")

    status_check()

    if first_status_input != '':
        status = first_status_input

    status_check()

    inventory[book_name] = status

    change_status_option = int(input("If you wish to change the status again press 1 else press 2: "))
    
    while change_status_option < 2:
        status = input("Enter the NEW status of the book (e.g. 'on shelf'/'checked out') and press ENTER: ")
        inventory[book_name] = status
        change_status_option = int(input("If you wish to change the status again press 1 else press 2: "))

    add_additional_books_prompt = input("Do you wish to add additional books (y or n)?: ")

    if add_additional_books_prompt == "y":
        library_system()
    else:
        return print(inventory)

library_system()




def status_check(status="on shelf"):
    while status !=  'on shelf' and status != 'checked out':  # Checks if user typed in anything but these two options. Anything else means this WILL execute.
        status = input("OOPS! Please check that you've typed out your selection correctly. Enter the status of the book (e.g. 'on shelf'/'checked out') and press ENTER: ")

    return status