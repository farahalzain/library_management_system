# Library Management System

## Overview

The **Library Management System** is a simple Python project that simulates a small library.
It allows users to:

* View all available items
* Search items by title
* Borrow items
* Reserve items
* Return items

This project demonstrates the use of **Object-Oriented Programming (OOP)** in Python with classes like `Library`, `User`, and `Item`.

---

## Project Structure

```
library_management_system/
│── library.py      # Contains the Library class (main logic)
│── user.py         # Contains the User class
│── item.py         # Contains the Item class
│── main.py         # Entry point of the program (menu system)
│── README.md       # Project documentation
```

---

## Features

* Add and manage users 
* Add and manage library items (books, etc.) 
* Borrow an item ---> Updates availability
* Reserve an item ---> Marks it as reserved
* Return an item ---> Makes it available again
* Search item by title 🔍

---

## Example Usage

```
--- Library System ---
1. View all items
2. Search item by title
3. Borrow an item
4. Reserve an item
5. Return an item
6. Exit

Enter your choice: 1
[1] Title: Python Basics | Available: Yes
[2] Title: Data Structures | Available: No (Borrowed by Ali)
```

---

## Future Improvements

* Add database support (SQLite / MySQL)
* Track due dates and late fees
* Add multiple item types (magazines, DVDs)
* User authentication system

---
