# a class derived from an already derived class is called multilevel inheritence
# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

#     def show_details(self):
#         print(f'Name: {self.name}')
#         print(f'Species: {self.species}')
        
# class Dog(Animal):
#     def __init__(self, name , breed):
#         Animal.__init__(self, name, species='Dog')
#         self.breed = breed
#     def show_details(self):
#         Animal.show_details()
#         print(f'Breed: {self.breed}')

# class GoldenRestriver(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self,name, breed = "Golden Restriver")
#         self.color = color

#     def show_details(self):
#         Dog.show_details(self)
#         print(f'color: {self.color}')
''''
class Animal:
    def __init__(self,name,specie):
        self.name = name
        self.specie = specie
    def show_Details(self):
        print(f'name   :{self.name}')
        print(f'specie :{self.specie}')

class Dog(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self, name, specie = 'Dog')
        self.breed = breed
    def show_Details(self):
       Animal.show_Details(self)
       print(f'breed  :{self.breed}')

class GermanShepherd(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = 'German Shepherd', )
        self.color = color
    def show_Details(self):
       Dog.show_Details(self)
       print(f'color  :{self.color}')

dogeshBhaya = GermanShepherd('sharu','brown')
dogeshBhaya.show_Details()
'''
class LivingThing:
    def __init__(self, name, kingdom):
        self.name = name 
        self.kingdom = kingdom
    def show_details(self):
        print(f'Name : {self.name}\nKingdom : {self.kingdom}')

class Animalia(LivingThing):
    def __init__(self, name, specie):
        LivingThing.__init__(self,name, kingdom = 'Animalia')
        self.specie = specie
    def show_details(self):
        LivingThing.show_details(self)
        print(f'specie: {self.specie}')

class Human(Animalia):
    def __init__(self, name, sex):
        Animalia.__init__(self,name, specie = "Human")
        self.sex = sex
    def show_details(self):
        Animalia.show_details(self)
        print('sex:',self.sex)

class Boy(Human):
    def __init__(self, name, age):
        super().__init__(name, sex = 'Male')
        self.age = age
    def show_details(self):
        # super().show_details()
        Human.show_details(self) # works same to the above one don't self it
        print(f'age: {self.age}')

Talha =Boy('Talha','21')
Talha.show_details()
print(Human.mro())