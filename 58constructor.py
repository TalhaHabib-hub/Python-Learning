class Person:
    def __init__(self,n,o): # constructor always return none
        print("Hey I am a person")
        self.name = n
        self.occ = o
    name = 'Talha'
    occ = "madina ka musafir"
    def info(self):
        print(f'{self.name} is {self.occ}')


a = Person("Allah", "Creater") 
b = Person("Talha", "Developer") # 3 arguments are passing here b as self also
a.info()
b.info()