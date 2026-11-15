print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))

# ---------- 2. OPERATORS & STRINGS ----------
print("\n=== 2. Operators & Strings ===")
a, b = 10, 3
print("Add:", a + b, "| Div:", a / b, "| Floor:", a // b, "| Mod:", a % b, "| Pow:", a ** b)
text = "  Hello Python  "
print(text.strip().upper())              # remove spaces, uppercase
print(f"{name} is {age} years old")      # f-string formatting
print("Python"[0], "Python"[-1], "Python"[1:4])  # indexing & slicing
#tried 
# ---------- 3. CONDITIONALS ----------
print("\n=== 3. Conditionals ===")
score = 78
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)

# ---------- 4. LOOPS ----------
print("\n=== 4. Loops ===")
for i in range(1, 4):                    # for loop with range
    print("for loop:", i)
count = 0
while count < 3:                         # while loop
    print("while loop:", count)
    count += 1
for i in range(10):
    if i == 2:
        continue                         # skip this iteration
    if i == 5:
        break                            # stop the loop
    print("i =", i, end=" ")
print()

# ---------- 5. DATA STRUCTURES ----------
print("\n=== 5. Data Structures ===")
fruits = ["apple", "banana", "cherry"]   # list: ordered, changeable
fruits.append("mango")
fruits.remove("banana")
print("List:", fruits)

point = (3, 4)                           # tuple: ordered, NOT changeable
x, y = point                             # unpacking
print("Tuple:", point, "x =", x, "y =", y)

student = {"name": "Ali", "age": 20}     # dict: key -> value
student["city"] = "Lahore"
print("Dict:", student, "| keys:", list(student.keys()))

unique = set([1, 2, 2, 3, 3, 3])         # set: unique items only
print("Set:", unique)

# ---------- 6. FUNCTIONS ----------
print("\n=== 6. Functions ===")
def greet(person, greeting="Hello"):     # default argument
    """Return a greeting message (this is a docstring)."""
    return f"{greeting}, {person}!"

def total(*numbers):                     # *args: any number of arguments
    return sum(numbers)

def show_info(**details):                # **kwargs: keyword arguments
    for key, value in details.items():
        print(f"  {key}: {value}")

print(greet("Talha"))
print(greet("Talha", greeting="Salam"))
print("Total:", total(1, 2, 3, 4))
show_info(language="Python", level="Intermediate")

def factorial(n):                        # recursion: function calls itself
    return 1 if n <= 1 else n * factorial(n - 1)
print("5! =", factorial(5))

# ---------- 7. COMPREHENSIONS, LAMBDA, MAP/FILTER ----------
print("\n=== 7. Comprehensions & Lambda ===")
squares = [n ** 2 for n in range(1, 6)]            # list comprehension
evens = [n for n in range(10) if n % 2 == 0]       # with condition
square_dict = {n: n ** 2 for n in range(1, 4)}     # dict comprehension
print(squares, evens, square_dict)

double = lambda n: n * 2                           # small anonymous function
print(list(map(double, [1, 2, 3])))                # apply to every item
print(list(filter(lambda n: n > 2, [1, 2, 3, 4]))) # keep matching items
words = ["pear", "fig", "banana"]
print(sorted(words, key=len))                      # sort by length

# ---------- 8. ERROR HANDLING ----------
print("\n=== 8. Error Handling ===")
def safe_divide(p, q):
    try:
        return p / q
    except ZeroDivisionError:                      # handle a specific error
        print("  Cannot divide by zero!")
        return None
    finally:
        print("  (division attempted)")            # always runs
print(safe_divide(10, 2))
print(safe_divide(10, 0))

try:
    int("abc")
except ValueError as err:
    print("ValueError caught:", err)

# ---------- 9. FILE HANDLING ----------
print("\n=== 9. File Handling ===")
import os
with open("demo.txt", "w") as f:                   # 'with' closes file automatically
    f.write("Line 1\nLine 2\nLine 3\n")
with open("demo.txt", "r") as f:
    for line in f:
        print("Read:", line.strip())
os.remove("demo.txt")                              # clean up

# ---------- 10. OOP: CLASSES & OBJECTS ----------
print("\n=== 10. OOP: Class & Object ===")
class Dog:
    species = "Canis familiaris"                   # class attribute (shared)

    def __init__(self, name, age):                 # constructor
        self.name = name                           # instance attributes
        self.age = age

    def bark(self):                                # method
        return f"{self.name} says Woof!"

    def __str__(self):                             # what print() shows
        return f"Dog({self.name}, {self.age})"

d1 = Dog("Rex", 3)
d2 = Dog("Bella", 5)
print(d1, "|", d1.bark(), "|", d2.species)

# ---------- 11. OOP: ENCAPSULATION ----------
print("\n=== 11. OOP: Encapsulation ===")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance                   # private (double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")  # raise our own error
        self.__balance -= amount

    @property                                      # read-only access via getter
    def balance(self):
        return self.__balance

acc = BankAccount("Talha", 100)
acc.deposit(50)
print("Balance:", acc.balance)
try:
    acc.withdraw(500)
except ValueError as err:
    print("Error:", err)

# ---------- 12. OOP: INHERITANCE & POLYMORPHISM ----------
print("\n=== 12. OOP: Inheritance & Polymorphism ===")
class Animal:                                      # parent (base) class
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Cat(Animal):                                 # child class
    def speak(self):                               # override parent method
        return f"{self.name} says Meow"

class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name)                     # call parent constructor
        self.color = color
    def speak(self):
        return f"{self.color} cow {self.name} says Moo"

for animal in [Cat("Tom"), Cow("Daisy", "Brown"), Animal("Generic")]:
    print(animal.speak())                          # same call, different result

# ---------- 13. OOP: ABSTRACTION ----------
print("\n=== 13. OOP: Abstraction ===")
from abc import ABC, abstractmethod

class Shape(ABC):                                  # abstract class
    @abstractmethod
    def area(self):                                # children MUST implement this
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return round(3.14159 * self.r ** 2, 2)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

for shape in (Circle(3), Rectangle(4, 5)):
    print(type(shape).__name__, "area:", shape.area())

# ---------- 14. OOP: MAGIC METHODS & STATIC/CLASS METHODS ----------
print("\n=== 14. Magic Methods ===")
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):                      # lets us use +
        return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):                       # lets us use ==
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    @staticmethod
    def dot(v1, v2):                               # no self needed
        return v1.x * v2.x + v1.y * v2.y

    @classmethod
    def zero(cls):                                 # alternative constructor
        return cls(0, 0)

v = Vector(1, 2) + Vector(3, 4)
print(v, v == Vector(4, 6), Vector.dot(Vector(1, 2), Vector(3, 4)), Vector.zero())

# ---------- 15. MINI PROJECT: TO-DO MANAGER ----------
print("\n=== 15. Mini Project: To-Do Manager ===")
class Task:
    def __init__(self, title, done=False):
        self.title, self.done = title, done
    def __str__(self):
        return f"[{'x' if self.done else ' '}] {self.title}"

class TodoList:
    def __init__(self):
        self.tasks = []                            # composition: list of Task objects
    def add(self, title):
        self.tasks.append(Task(title))
    def complete(self, title):
        for t in self.tasks:
            if t.title == title:
                t.done = True
                return
        print(f"Task '{title}' not found")
    def show(self):
        for t in self.tasks:
            print(t)

todo = TodoList()
todo.add("Learn variables")
todo.add("Learn functions")
todo.add("Learn OOP")
todo.complete("Learn variables")
todo.complete("Learn functions")
todo.show()