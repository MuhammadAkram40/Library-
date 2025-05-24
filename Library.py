class Library:
    def __init__(self, book_list):
        self.books = book_list
        self.lend_data = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, book, user):
        if book in self.books:
            if book not in self.lend_data:
                self.lend_data[book] = user
                print(f"\n'{book}' has been lent to {user}.")
            else:
                print(f"\nSorry, '{book}' is already lent to {self.lend_data[book]}.")
        else:
            print(f"\nSorry, '{book}' is not in the library collection.")

    def add_book(self, book):
        self.books.append(book)
        print(f"\n'{book}' has been added to the library.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"\n'{book}' has been returned.")
        else:
            print(f"\n'{book}' was not lent out.")

def main():
    library = Library(["Python Programming", "Data Science", "Machine Learning", "Deep Learning"])
    
    while True:
        print("\n===== Library Menu =====")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            book = input("Enter the book name: ")
            user = input("Enter your name: ")
            library.lend_book(book, user)
        elif choice == '3':
            book = input("Enter the book name to add: ")
            library.add_book(book)
        elif choice == '4':
            book = input("Enter the book name to return: ")
            library.return_book(book)
        elif choice == '5':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
