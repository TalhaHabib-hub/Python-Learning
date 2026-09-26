class Animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species 

    def make_sound(self):
        print('sound made by the animal')

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species='dog')
        self.breed = breed

    def make_sound(self):
        print('Bark')

d = Dog("Dog","Doguuu")
d.make_sound()

a = Animal('dog', 'animi')
a.make_sound()
'''Single Inheritance in python
single inheritence is a type of inheritence where a class inherits form a parent class, simply specify the parent class in the class definition, inside the paranthesis'''

#  The dog class inherits all the attributes and behaviors of the animal class, including the __init__ and the make_sound method. Additionally, Dog class has it's own __init__ method that adds a new attribute for the breed of the dog, and it also overrides the make_sound method to specify the sound that a dog makes.
# Single inheritence is a powerful tool in python that allows you to create new classes based on existing classes. It allows you to reuse the code, extend it to fit your needs, and make it easier to meange complex systems. Understanding single inheritance is an important step in becoming proficient in object oriented programming
'''Q1 : Implement a cat class by using the animal class. Add some methods specific to cat'''
class Cat(Animal):
    def __init__(self, name, kind):
        # Animal.__init__(self,name, species='cat')  # Sir introduced it I found that the code is running even without it
        self.kind = kind

    def make_sound(self):
        print('meow')
c = Cat('bilu','bilkhan')
c.make_sound()
