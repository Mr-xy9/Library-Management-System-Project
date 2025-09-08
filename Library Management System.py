books = ["Book 1", "Book 2", "Book 3", "Book 4", "Book 5", "Book 6"]

while True:
    print("1. Add a book")
    print("2. Show all books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Exit")

    c = input("Choose: ")

    if c == "1":
        name = input("Enter book name: ")
        books.append(name)
        print("Book added successfully.")

    elif c == "2":
            for b in books:
                print(b)

    elif c == "3":
        name = input("Enter book name to search: ")
        if name in books:
            print("Book found:", name)
        else:
            print("Book not found.")

    elif c == "4":
        name = input("Enter book name to delete: ")
        if name in books:
            books.remove(name)
            print("Book deleted successfully.")
        else:
            print("Book not found to delete.")

    elif c == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
