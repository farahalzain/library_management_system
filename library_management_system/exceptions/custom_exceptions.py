class ItemNotAvailableError(Exception):
    def __init__(self, message="Item is not available now"):
        super().__init__(message)

class UserNotFoundError(Exception):
    def __init__(self, message="User is not found"):
        super().__init__(message)

class ItemNotFoundError(Exception):
    def  __init__(self, message = "Item is not found"):
        super().__init__(message)