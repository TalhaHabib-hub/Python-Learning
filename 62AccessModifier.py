# by default public
class Employee:
    def __init__(self):
        self.__name = "Harry"
a = Employee()

print(a._Employee__name) # cannot be accessed directly
# print(a.name) 
print(a.__dir__())

class Student:
    def __init__(self):
        self._name = "Talha"

    def _funName(self):
        return "Talha with Puropose"
    
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())

'''
Access Specifier/Modifiers
Access specifier or access modifiers in python programming are used to limit the access of class variables and class mehtods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:

Types of access specifiers
1. Public access modifiers.
2. Privater access modifier.
3. Protected access modifier.
'''

#1. Public access modifiers.
'''All the variables and methods( member functions) in python are by default public. Any instance variable in a class followed by th e 'self' keyword'''

# 2. Privater access modifier.
'''By definition, Private members of a class (variable or methods) are those members which are only accessible inside the class. We cannot use private members outside the class.

In python, there is no strict concepts of 'private' access modifiers like in some other languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with underscore(_). This is known as a 'weak internal use indicator' and it is a convention only. not a strict rule. Code outside the class can still access these private variables and methods, but it is generally that should not be accessed or modified'''

'''Private members of a class cannot be accessed or inherited outside of class. if we try to access or to inherit the properties of private members to child class(derived class). Then it will show the error'''

## name Mangling
'''name Mangling in python is a technique used to protect class-private and and superclass-private attributes form being accidently overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively'''
# in the example the __name is a private varaible/ attribute but can still be accessed from outside the class. The attribute _Employee__name by this way can be accessed directly