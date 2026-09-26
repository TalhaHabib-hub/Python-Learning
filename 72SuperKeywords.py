class ParentClass:
    def parent_method(self):
        print("This is the parent method")

class childClass(ParentClass):
    def child_method(self):
        print("This is the child method")

        super().parent_method()

child_object = childClass()
child_object.child_method()

child_object.parent_method()
'''_________Super keyword in python____________
The super() keyword in python is used to refer to parent class. it is especially useful when a class inherits form multiple parent classes and you want to call a method from one of the parent classes

When a class inherits from a parent class, it can override or extend the methods defined in the parent class, However, sometimes you might want to use the parent class method in the child class. This is where super() keyword comes in handy
'''
print('____________________________________________________')
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def parentMethod():
#         print("I am parent method")
# class Programmer:
#     def __init__(self, name, id, lang):
#         self.name = name
#         self.id = id
#         self.lang = lang
    
# Rahan = Employee("rohan Das", 343)
# Talha = Programmer("harry",2342,"python")

# ## look with focus that things are repeating I will follow the dry principle the don't repeat yourself yourself
'''so below in the below class I am calling the Employee class with super method'''

class Employee: # super class
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang = lang
    
Rahan = Employee("rohan Das", 343)
Talha = Programmer("Talha",2342,"python")
print(Rahan.name)
print(Talha.name)
print(Talha.id)
print(Talha.lang)

class Habib:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class Talha(Habib):
    def __init__(self,name,age,lang):
        super().__init__(name,age)
        self.lang = lang

abdullah = Talha("Abdullah",23,"Python")
print(abdullah.age)
print(abdullah.name)
print(abdullah.lang)
