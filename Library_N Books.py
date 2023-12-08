#Experiment-3 input code


class Book:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost

def delete_duplicates(books):
    unique_books = list(set(books))
    return unique_books

def display_books_in_ascending_order(books):
    sorted_books = sorted(books, key=lambda x: x.cost)
    return sorted_books

def count_expensive_books(books):
    expensive_books_count = sum(1 for book in books if book.cost > 500)
    return expensive_books_count

def copy_books_less_than_500(books):
    less_than_500_books = [book for book in books if book.cost < 500]
    return less_than_500_books

# Example data
book1 = Book("Book A", 300)
book2 = Book("Book B", 450)
book3 = Book("Book C", 700)
book4 = Book("Book D", 250)
book5 = Book("Book E", 600)

# List of books
library_books = [book1, book2, book3, book4, book5]

# a) Delete duplicate entries
unique_books = delete_duplicates(library_books)
print("Unique Books:")
for book in unique_books:
    print(f"{book.title}: Rs{book.cost}")

# b) Display books in ascending order based on cost of books
sorted_books = display_books_in_ascending_order(library_books)
print("\nBooks in Ascending Order of Cost:")
for book in sorted_books:
    print(f"{book.title}: Rs{book.cost}")

# c) Count number of books with cost more than 500
expensive_books_count = count_expensive_books(library_books)
print(f"\nNumber of Books with Cost more than Rs500: {expensive_books_count}")

# d) Copy books in a new list which has cost less than 500
less_than_500_books = copy_books_less_than_500(library_books)
print("\nBooks with Cost less than Rs500:")
for book in less_than_500_books:
    print(f"{book.title}: Rs{book.cost}")
