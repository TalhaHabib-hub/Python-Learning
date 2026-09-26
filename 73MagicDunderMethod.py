'''magic / dunder methods in python
These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour

Magic methods, also known as 'dunders' from the double underscores surrounding their name, are powerful tools that allow you to customize the behavior of your classes.They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties'''
class Employee:
    name = "Talha"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
        # return len(self.name)
    
e  = Employee()
print(e.name)
print(len(e))
print(e.__len__())

# the init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object's initial state, and it is where you would typically define any instance variables that you need. Also called constructor, we have discussed this method already
'''The str and repr methods are both us ed to convert an object to a string reperestation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object'''
class Banda:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"(str)->The name of the Employee is: {self.name}"
    def __repr__(self): 
        return f"(repr)->The name of the Employee is: {self.name}"
    def __call__(self): # obj()
        print("kicha la Talha")
    # when you commented the above two line the result on screen for print(B) -- <__main__.Banda object at 0x0000022777748830> so the __str__ work is to tell clearly about the object other wise printing the object was giving not such information
B = Banda("Yasir")
print(B) # when we do this it will look for the str if it doesn't find str it goes to  repr ( which is exactly the same as str just write repr instead of repr)
# print(B.repr)  # not like this
print(repr(B))
# print(B.str)   #not like this
print(str(B))
B() # if I just want to call the object the __call__ will be executed