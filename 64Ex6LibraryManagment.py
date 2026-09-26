'''Write a library class with no_of_books and books as two instance variables. Write a program to create a library from this library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesn't persist the book after the program is stopped!'''

class Library:
    def __init__(self, L, n):
        self.no_of_books = n
      
        self.books = L

    def add_Book(self,book):
      
        self.no_of_books+=1
        self.books.append(book)

    def check(self):
        print('No of Books =',self.no_of_books,'length of List =',len(self.books))
        if self.no_of_books == len(self.books):
            return True
        else:
            return False
intialList = ['DLD','QR','OOP']
a = Library(intialList,len(intialList))
a.add_Book('Sociology')
a.add_Book('Sociology2')
a.add_Book('Sociology3')

if a.check() == True:
    print("Prgramming is going well")
else:
    print("Some Short comings in Program")
print(a.books)
