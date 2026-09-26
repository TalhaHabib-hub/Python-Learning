class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showinfo(self):
        print(f'The Library has {self.noBooks} Books. The books are {self.books}')

    

l1 = Library()
l1.addBook("Harry potter")
l1.addBook("Harry potter1")
l1.addBook("Harry potter2")
l1.showinfo()