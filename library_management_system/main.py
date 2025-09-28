from library import Library
from models.reservable import Reservable
from models.library_item import LibraryItem
from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine
from models.user import User
import json
from exceptions.custom_exceptions import ItemNotAvailableError, UserNotFoundError, ItemNotFoundError

def main():
    library = Library()
    library.load_data()
    
    while True:
        print("\nWelcome to the Library System")
        print("1. View all available items")
        print("2. Search item by title")
        print("3. Register as a new user")
        print("4. Borrow an item")
        print("5. Reserve an item")
        print("6. Return an item")
        print("7. Exit and Save")

        choice = input("Select a choice (1-7): ").strip()
        try:
            if choice == "1":
                if library.items:
                    print("****Library****")
                    for item in library.items:
                        item.display_info()
                    
            elif choice == "2":
                keyword = input("Enter your item name or type : ")
                results = [item for item in library.items if keyword in item.title.lower() or keyword in item.__class__.__name__.lower()]
                if results:
                    for item in results:
                        print(item.display_info())
                else:
                    print("No matching items.")

            elif choice == "3":
                print("****Registing New User****")
                name = input("Your name: ")
                email = input("Your email: ")
                user_id = f"user{len(library.users)+1}"
                user = User(user_id, name, email)
                library.add_user(user)
                print(f"New user is registed with id: {user_id}")

            elif choice == '4':
                try:
                    print("****Borrowing****")
                    user_id =input("Enter the id user:  ")
                    item_id =input("Enter the id item: ")
                    library.borrow_item(user_id, item_id)
                    print("Item is borrowed successfuly")
                except Exception as e : 
                    print(f" Error: {e}")
                    
            elif choice == "5":
                try:
                    print("****Reservaing****")
                    user_id =input("Enter the id user:  ")
                    item_id =input("Enter the id item: ")
                    library.reserve_item(user_id, item_id)
                    print("Item is reservaed successfully.")
                except Exception as e:
                    print(f" Error: {e}")
                    
            elif choice == '6':
                try:
                    print("****Returning****")
                    user_id = input("Enter the id user:  ")
                    item_id =input("Enter the id item: ")
                    library.return_item(user_id, item_id)
                    print("Item is returned successfully.")
                except Exception as e:
                    print(f" Error: {e}")
                    
            elif choice == "7":
                try:
                    library.save_data()
                    print("Goodbye!")                    
                    break
                except Exception as e:
                    print(f"Error during Saving: {e}")

            else:
                print("Invalid choice.")
                
        except (ItemNotFoundError, UserNotFoundError, ItemNotAvailableError, Exception) as e:
            print(" Error:", str(e))
            
        finally:
            print("------------")
            
if __name__ == "__main__":
    main()