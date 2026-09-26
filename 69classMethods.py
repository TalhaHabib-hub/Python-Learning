class Employee:
    company = 'apple'
    def show(self):
        print(f'The name is {self.name} and company is {self.company}')
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Talha"
e1.show()
e1.changeCompany('Tesla')
# e1.company = "Tesla" # I can do this with it why was the function making neede
e1.show()
print(Employee.company) # Till here i understand that the value of the company is changed for just the instance do actually changed the value of the company just write @classmethod over the changer function
e = Employee()
e.name='Yashfa'
e.changeCompany('Bords')
e.show()

# Why use python class methods?
'''class methods are useful several situations. for example, you might want to create a factory method that creates instances of your class in a specific way. YOU could define a class method that creates the instances and returns it to the caller. another common use is to provide alternative constructors for your class in multiple ways. but still have a consistent interface for doing so.
'''
#How to use python class methods
'''
To define a class method, you simply use the '@classmethod' docorator before the method definition. The first argument of the method should always be 'cls' which represents the class itself.
'''
'''
Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creatiing factory mehods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in python.

Talha I saw something new here
'''
ali , sajid = "talha, kasaho".split(",")
print(ali,sajid)
# I hadn't seen this before # just use two varialbles write them one after one another the return list's element will be assigned to each value sequencely