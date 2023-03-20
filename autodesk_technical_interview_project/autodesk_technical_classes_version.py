import time

class LibraryInventory:
    def __init__(self):
        self.inventory = {}

    def new_book(self):
        title_input1 = input("\nEnter the title of the book: ").upper()
        # check for duplicate book entries; if entry is a duplicate, user sent to main menu
        if title_input1 in self.inventory:
            print("\nSorry, that title is already in the inventory.")
            return
        else:
            title = title_input1

        # check for invalid num input
        invalid_nums = [0, 3, 4, 5, 6, 7, 8, 9]
        number_pressed = int(input("\nEnter 1 to mark book as 'on shelf' and 2 to mark as 'checked out': "))
        if number_pressed in invalid_nums:
            while number_pressed != 1 and number_pressed != 2:
               print("\nOOPS! You entered the wrong number please try again.")
               number_pressed = int(input("\nEnter 1 to mark book as 'on shelf' and 2 to mark as 'checked out': "))

        if number_pressed == 1:
            status = "on shelf"
        else:
            status = "checked out"
        
        self.inventory[title] = status

        print(f"\nHere is your inventory with your recent addition: {self.inventory}\n")


    def remove_book(self):
        print(f"\nHere is your book inventory: {self.inventory}")
        book_to_delete = None
        # check for empty inventory; if inventory is empty, user sent to main menu
        if len(self.inventory) == 0:
            print("\nHmm... It looks like your inventory is empty.")
            time.sleep(3)
            return

        book_to_delete = input("\nWhat book would you like to delete from your inventory?: ").upper()   
        # check to ensure book is present within inventory; if book not present, user sent to main menu  
        if book_to_delete not in self.inventory:
            print("\nHmm... It looks like that book doesn't exist in your inventory.")
            time.sleep(3)
            return
        
        delete_prompt_answer = input(f"\nAre you sure you want to delete '{book_to_delete}' from your inventory (y or n)?: ")
        if delete_prompt_answer == 'y':
            del self.inventory[book_to_delete]
        else:
            return
        
    def change_status(self):
        print(f"\nHere is your book inventory: {self.inventory}")
        book_to_change = None
        # check for empty inventory; if inventory is empty, user sent to main menu
        if len(self.inventory) == 0:
            print("\nHmm... It looks like your inventory is empty.")
            time.sleep(3)
            return

        book_to_change = input("\nWhat book would you like to change the status of?: ").upper()   
        # check to ensure book is present within inventory; if book not present, user sent to main menu  
        if book_to_change not in self.inventory:
            print("\nHmm... It looks like that book doesn't exist in your inventory.")
            time.sleep(3)
            return
        
        change_status_prompt_answer = input(f"\nAre you sure you want to change the status of '{book_to_change}' from your inventory (y or n)?: ")
        if change_status_prompt_answer == 'y':
            # check for invalid num input
            invalid_nums = [0, 3, 4, 5, 6, 7, 8, 9]
            number_pressed = int(input("\nEnter 1 to mark book as 'on shelf' and 2 to mark as 'checked out': "))
            if number_pressed in invalid_nums:
                while number_pressed != 1 and number_pressed != 2:
                    print("\nOOPS! You entered the wrong number please try again.")
                    number_pressed = int(input("\nEnter 1 to mark book as 'on shelf' and 2 to mark as 'checked out': "))

            if number_pressed == 1:
                status = "on shelf"
            else:
                status = "checked out"
            
            self.inventory[book_to_change] = status
            print(f"Your new inventory is:")
        else:
            return
        







def main():
    library_inventory = LibraryInventory()                              # creates instance of LibraryInventory(), which is an empty dict
    number_pressed = None
    while number_pressed != '5':
        number_pressed = input("\nChoose an option from the list below:\n\
            1. Add a book.\n\
            2. Remove a book.\n\
            3. Modify an existing book's status.\n\
            4. View your list of checked out books.\n\
            5. Exit\n")
        
        if number_pressed == '1':            # 1. Option to add a book
            library_inventory.new_book()
        elif number_pressed == '2':          # 1. Option to remove a book
            library_inventory.remove_book()
        elif number_pressed == '3':
            library_inventory.change_status()

    



if __name__ == "__main__":
    main()