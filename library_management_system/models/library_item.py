from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, item_id, title, author, is_available= True):
        self.item_id = int(item_id)
        self.title = title
        self.author = author
        self.is_available = is_available

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.is_available