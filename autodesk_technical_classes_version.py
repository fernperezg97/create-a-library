class LibraryInventory:
    def __init__(self):
        self.inventory = {}

    def new_book(self, title, status):
        title_input1 = input("Enter the title of the book: ")
        if title_input1 in self.inventory:
            while title_input1 in self.inventory:
                print("\nSorry, that title is already in the inventory. Try adding a new title.\n")
                LibraryInventory.new_book()
        else:
            title = title_input1

        invalid_nums = [0, 3, 4, 5, 6, 7, 8, 9]
        number_pressed = input("Enter 1 to mark book as 'on shelf' and 2 to mark as 'checked out': ")
        if number_pressed in invalid_nums:
            while number_pressed != 1 or number_pressed != 2:
               print("OOPS! You entered the wrong number please try again.")
        elif number_pressed == 1:
            status = "on shelf"
        elif number_pressed == 2:
            status = "checked out"
        else:
            status = "on shelf"
        
        self.inventory[title] = status

        print(f"Here is your inventory: {self.inventory}")

        add_additional_books_prompt = input("\nDo you wish to add more books (y or n)?")
        if add_additional_books_prompt == 'y':
            LibraryInventory.new_book()
        else:
            where_to_next_prompt = input("\nTo go back to the main page press 'm' otherwise press 'q' to quit the program.")

    def remove_book(self, title):
        print(f"Here is your book inventory: {self.inventory}")
        book_to_delete = input("\nWhat book would you like to delete from your inventory?: ".upper())
        if len(self.inventory) == 0:
            print("\nYour inventory is empty! Press 'm' to go back to the main menu or press 'q' to quit: ")
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
                else:


        







def main():
    library_inventory = LibraryInventory()
    print("Choose an option from the list below:\
          1. Add a book.\
          2. Remove a book.\
          3. Modify an existing book's status.\
          4. View your list of checked out books.\
          5. Exit")

    print("Choose an option")
    number_pressed = input()

    # 1. Add a book
    if number_pressed == 1:
        LibraryInventory.new_book()






    library2 = LibraryInventory()

    



if __name__ == "__main__":
    main()