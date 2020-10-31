# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# Sam_Library = Library(list_of_books, library_name)


# dictionary (books-name_of_person)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self, list1, name):
        self.books = list1
        self.name = name
        self.lendDict = {}

    def display_book(self):
        print(f"The books available in the library are {self.books}")

    def lend_book(self, book, name):
        if book not in self.lendDict.keys():
            print("Book is available \n Enter the number of days to borrow:")
            no_of_days = int(input())
            print(f"You should kindly return this book in {no_of_days}.")
            self.books.remove(book)
            self.lendDict.update({book: name})
            print("The lender book database has been updated! You can take your book now")
        else:
            print(f"Sorry! The book {book} is not available in the library. Since it is already borrowed by "
                  f"{self.lendDict[book]}")

    def add_book(self, book):
        self.books.append(book)
        print("Thanks for donating this book to the library!")

    def return_book(self, book):
        self.books.append(book)
        print("Thanks for returning the book! See you again!")


if __name__ == '__main__':
    Sam_library = Library(['Rise of the Dragons', 'Until we meet again', 'Journey from dawn to dusk',
                           'The pocket love story'], "Good Reads Library")
    while True:
        print(f"Welcome to the {Sam_library.name}.")
        choice1 = int(input('Enter \n 1 - To display books\n 2 - To borrow book\n 3 - To donate book\n 4 - To return '
                            'the '
                            'book\n'))
        if choice1 == 1:
            Sam_library.display_book()
        elif choice1 == 2:
            user = input("Enter your name: ")
            book_name = input("Enter the name of the book you want to borrow: ")
            Sam_library.lend_book(book_name, user)
        elif choice1 == 3:
            book_name = input("Enter the name of the book you want to donate to the library: ")
            Sam_library.add_book(book_name)
        elif choice1 == 4:
            book_name = input("Enter the name of the book you want to return: ")
            Sam_library.return_book(book_name)
        else:
            print("Not a valid option!")

        choice2 = ""
        while choice2 != 'Q' and choice2 != 'C':
            choice2 = input("Press Q to quit\n Press C to continue")
            if choice2 == 'Q':
                exit()
            elif choice2 == 'C':
                continue
