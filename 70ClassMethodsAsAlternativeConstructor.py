'''how to use class methods as alternative  constructor'''
# In the object oriented programming, the term constructor refers tok a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.
''# However, there are times when you want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructor is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes "name" and 'age'. The default constructor for the class look like this
class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

e = Employee('Talha',12000)
print(e.name)
print(e.salary)
# Talha sorry for bothering we were happy with using our constructor normally but sometime what happens is like the user gives us the data wholey in the form of string but we can not give them to the object interm of class so for fullfilling that purpose we use the class methods as alternative constructor.
# lets say the person give me the both the requirments in string form
string = "TalhaHabib-12939399"
# no problem Talha I am here
e2 = Employee(string.split("-")[0],string.split('-')[1])
'''Talha if split a strin we actually gets a list'''
print(e2.name)
print(e2.salary)
'''Talha though you understand why is this one happening but still seem not to be like a good programming skill it is code to much lets do it more efficiently'''
# lets common Talha we are going to solve it with using class methods
class Human:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
# Talha here we handle the issue if the user gives us in string form we will use class method
    @classmethod
    def fromStr(cls, string): # running this function if the string is input
        return cls(string.split('-')[0], string.split('-')[1])
string = "kahan-10000"
H1 = Human.fromStr(string)
# aik class method sa app undo class ka sath parameteron ko rawana kar rahan han class say dot laga kar or wo object return kar rahan han not as usuall
'''I Think ma samaj gaya mana class method ko use karna kalia palha tag laga kar class ka andar hi bata dia ka bhai ya aik class method ha phir aik varible banaya usa kuch dana ka lia mana class. karka class ka method kok access kia asa class.classMetho or us method ko mana aik string as a parameter pass kia jis wo split karka magar istarah karka us varible ma return karga jis tarah woh use ka qabil ho jaya'''
print(H1.name)
class khan :
    def __init__(self,name,kaam):
        self.name = name
        self.kaam = kaam
    @classmethod
    def objReturner(cls,string):
        return cls(string.split('-')[0],string.split('-')[1])
obj = khan.objReturner('Talha-will be the best')
print(obj.name)
print(obj.kaam)