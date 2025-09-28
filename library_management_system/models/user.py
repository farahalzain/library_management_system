class User:
    def __init__(self, user_id, name, email, borrowed_items=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = borrowed_items if borrowed_items else []
        self.email = email
    def display_info(self):
        print(f"User: {self.name} | ID: {self.user_id} | Email: {self.email}" )
        if self.borrowed_items:
            print(f"Borrowed Items:")
            for item in self.borrowed_items:
                item.display_info()
        else:
            print("No borrowed items.")
            
    def borrow_item(self, item):
        if str(item.item_id) not in self.borrowed_items:
            self.borrowed_items.append(str(item.item_id))

    def return_item(self, item):
        if str(item.item_id) in self.borrowed_items:
            self.borrowed_items.remove(str(item.item_id))


            
            
            
            
            
            