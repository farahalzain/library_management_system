from models.reservable import Reservable
from models.library_item import LibraryItem
from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine
from models.user import User
import json
from exceptions.custom_exceptions import ItemNotAvailableError, UserNotFoundError, ItemNotFoundError

class Library:
    def __init__(self):
        self.items = []
        self.users = []

    #### Items Management 
    def add_item(self, item):
        self.items.append(item)
        self.save_data()
        
    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                self.save_data()
                return
        raise ItemNotFoundError(f"The item with the ID {item_id} does not exist.")
    
    def get_item_by_id(self, item_id):
        for item in self.items:
            if str(item.item_id) == str(item_id):   
                return item
        raise ItemNotFoundError(f"The item with the ID {item_id} does not exist.")
    
    #### Users Management 
    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_data()
                return
        raise UserNotFoundError(f"The user with the ID {user_id} does not exist.")
    
    def get_user_by_id(self, user_id):
        for user in self.users:
            if str(user.user_id) == str(user_id): 
                return user
        raise UserNotFoundError(f"The user with the ID {user_id} does not exist.")

    
    #### Borrowing
    def borrow_item(self, user_id, item_id):
        user = self.get_user_by_id(user_id)
        item = self.get_item_by_id(item_id)

        if not item.check_availability():
            raise ItemNotAvailableError(f"The item {item.title} is currently unavailable.")

        item.is_available = False
        user.borrow_item(item)   
        print(f"{user_id} borrowed {item.title}")
        self.save_data()

    #### Returning
    def return_item(self, user_id, item_id):
        user = self.get_user_by_id(user_id)
        item = self.get_item_by_id(item_id)

        if not user or not item:
            print("Error: Cannot return, check user or item!")
            return

        item.is_available = True
        user.return_item(item)
        print(f"{user_id} returned {item.title}")
        self.save_data()
    
    #### Reserving
    def reserve_item(self, user_id, item_id):
        user = self.get_user_by_id(user_id)
        item = self.get_item_by_id(item_id)

        if isinstance(item, Reservable):
            item.reserve(user_id)
            print(f"{user.name} reserved {item.title}")
            self.save_data()
        else:
            raise Exception("This item does not support booking.")
        
    ##############################
    # Loading Data from JSON files
    def load_data(self, items_file='items.json', users_file='users.json'):
        try:
            with open(items_file, 'r') as f:
                items_data = json.load(f)
                for item in items_data:
                    if item['type'] == 'book':
                        self.items.append(Book(
                            item_id=item['item_id'],
                            title=item['title'],
                            author=item['author'],
                            pages=item.get('pages', 0),
                            is_available=item['is_available']
                        ))
                    elif item['type'] == 'dvd':
                        self.items.append(DVD(
                            item_id=item['item_id'],
                            title=item['title'],
                            author=item['author'],
                            duration=item.get('duration', 0),
                            is_available=item['is_available']
                        ))
                    elif item['type'] == 'magazine':
                        self.items.append(Magazine(
                            item_id=item['item_id'],
                            title=item['title'],
                            author=item['author'],
                            issue_number=item.get('issue_number', 0),
                            is_available=item['is_available']
                        ))
                        
            with open(users_file, 'r') as f:
                users_data = json.load(f)
                for user in users_data:
                    self.users.append(User(
                        user_id=user['user_id'],
                        name=user['name'],
                        email=user['email'],
                        borrowed_items=user.get('borrowed_items', [])
                    ))
        except FileNotFoundError:
            print("Data file not found. Creating a new one.")
        except Exception as e:
            print(f"Error loading data: {e}")

        
    ##############################
    # Save Data to the JSON files
    def save_data(self, items_file='items.json', users_file='users.json'):
        try:
            with open(items_file, 'w') as f:
                json.dump([self.serialize_item(item) for item in self.items], f, indent=2)

            with open(users_file, 'w') as f:
                json.dump([user.__dict__ for user in self.users], f, indent=2)

        except Exception as e:
            print("There Is Wrong while saving the data : ", str(e))

    def serialize_item(self, item):
        data = item.__dict__.copy()
        if isinstance(item, Book):
            data['type'] = 'book'
        elif isinstance(item, DVD):
            data['type'] = 'dvd'
        elif isinstance(item, Magazine):
            data['type'] = 'magazine'
        return data
