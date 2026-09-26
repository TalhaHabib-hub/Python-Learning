class person:
    name = "Talha"
    occupation = "Software Developer"
    networth = 10
    def info(self): # The self parameter is a reference to the current instance of the class, and is used to access variable that belongs to the class
        print(f'{self.name} is a {self.occupation}')

a = person()
print(a) #<__main__.person object at 0x000001F8125D8830>
# print(a.name)
a.name = "yasir"
a.occupation = 'AI Engineer'
a.info
# print(a.name,a.occupation,a.networth)

b = person()
b.name = 'Talha'
b.occupation = "ghulama madani"
b.networth = 99
b.info()

c = person()
c.info()

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(self.name,'is Taking')

p1= Person('Talha')
p1.talk()

import Talha57friend

Talha57friend.largest_in_Tuple(3,254,4,32)
