from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self,item_id, title, author, issue_number, is_available=True):
        super().__init__(item_id, title, author, is_available)
        self.issue_number = int(issue_number)

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"[Magazine] {self.title} by {self.author} | Issue: {self.issue_number} | Status: {status}")

        
