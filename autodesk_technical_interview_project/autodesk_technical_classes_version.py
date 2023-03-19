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


    def remove_book(self, title):
        print(f"Here is your book inventory: {self.inventory}")
        book_to_delete = input("\nWhat book would you like to delete from your inventory?: ").upper()
        if len(self.inventory) == 0:
            menu_or_quit = input("\nYour inventory is empty! Press 'm' to go back to the main menu or press 'q' to quit: ")
            # if menu_or_quit == 'm':
                
        elif book_to_delete not in self.inventory:
            print("Hmm... It looks like that books doesn't exist in your inventory.")
        else:
            print(f"Here is your book inventory: {self.inventory}")
            book_to_delete = input("\nWhat book would you like to delete from your inventory?: ")
            if book_to_delete in self.inventory == True:
                title = book_to_delete
                delete_prompt_answer = input(f"Are you sure you want to delete '{title}' from your inventory (y or n)?")
                if delete_prompt_answer == 'y':
                    del self.inventory[title]
                # else:


        







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
        
        # 1. Add a book
        if number_pressed == '1':
            library_inventory.new_book()
        elif number_pressed == '2':
            library_inventory.remove_book()
        # elif number_pressed == '3':

    



if __name__ == "__main__":
    main()