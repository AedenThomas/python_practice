# Given the list books_list = [["Java", "$128"], ["C++", "$99"], ["Python", "$169"]]
# Write an interactive program to perform the following operations.
# 1. Add a new book
# 2. search a book, take input from user
# 3. display the list
# 4. delete a book
# 5. exit

books_list = [["Java", "$128"], ["C++", "$99"], ["Python", "$169"]]

while True:
    print("1. Add a new book")
    print("2. Search a book")
    print("3. Display the list")
    print("4. Delete a book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_name = input("Enter the book name: ")
        book_price = input("Enter the book price: ")
        books_list.append([book_name, book_price])
        print("Book added successfully")

    elif choice == 2:
        book_name = input("Enter the book name: ")
        for book in books_list:
            if book[0] == book_name:
                print("Book found")
                print("Cost of the book is: ", book[1])
                break
        else:
            print("Book not found")

    elif choice == 3:
        print(books_list)
        
    elif choice == 4:

        book_name = input("Enter the book name: ")
        for book in books_list:
            if book[0] == book_name:
                books_list.remove(book)
                print("Book deleted successfully")
                break
        else:
            print("Book not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")