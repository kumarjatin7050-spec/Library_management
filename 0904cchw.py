# LIBRARY USING DICTIONARY

books = {}   

# ADD BOOKS
def add_books():
    name = input("Enter Book Name: ")
    books[name] = "Available"
    print("Book Added !")

# SHOW BOOKS
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Books List:")
        for name, status in books.items():
            print(name, "->", status)

# ISSUE BOOKS
def issue_books():
    name = input("Enter the book name: ")
    if name in books:
        if books[name] == "Available":
            books[name] = "Issued"
            print("Book Issued")
        else:
            print("Book already issued")
    else:
        print("Book not found")

# RETURN BOOKS
def return_books():
    name = input("Enter the book name: ")
    if name in books:
        if books[name] == "Issued":
            books[name] = "Available"
            print("Book Returned")
        else:
            print("Book was not issued")
    else:
        print("Book not found")

# MAIN BODY
def library():
    while True:
        print("\n1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank You !")
            break
        else:
            print("Invalid Choice !")

library()