from models.library_item import LibraryItem
from models.reservable import Reservable
from exceptions.custom_exceptions import ItemNotAvailableError, ItemNotFoundError

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, pages, is_available=True):
        super().__init__(item_id, title, author, is_available)
        self.pages = pages
        self.reserved_by = None

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        reserved = f'Reserved by: {self.reserved_by}' if self.reserved_by else "" 
        print(f"[Book] {self.title} by {self.author} | Pages: {self.pages} | Status: {status}{reserved}")

    def reserve(self, user_id):
        if self.reserved_by:
            raise ItemNotFoundError("This book is already reserved!")  
        if not self.is_available:
            raise ItemNotAvailableError("This book is not available.")
        else:
            self.reserved_by = user_id
