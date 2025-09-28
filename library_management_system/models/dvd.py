from models.library_item import LibraryItem
from models.reservable import Reservable
from exceptions.custom_exceptions import ItemNotAvailableError, ItemNotFoundError

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration, is_available= True):
        super().__init__(item_id, title, author, is_available)
        self.duration = int(duration)
        self.reserved_by = None

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        reserved = f", Reserved by: {self.reserved_by}" if self.reserved_by else ""
        print(f"[DVD] {self.title} by {self.author} | Duration: {self.duration} min | Status: {status}")

    
    def reserve(self, user_id):
        if self.reserved_by:
            raise ItemNotFoundError("This DVD is already reserved!")  
        if not self.is_available:
            raise ItemNotAvailableError("This DVD is not available.")
        else:
            self.reserved_by = user_id
            print(f"{self.title} reserved by {user_id}")
            