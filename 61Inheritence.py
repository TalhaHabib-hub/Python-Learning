class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f'The name of Employee: {self.id} is {self.name}')

class Programmer(Employee):
    def showLanguage(self):
        print(f'The default language is Python')

e1 = Employee('Rohan', 400)
e1.showDetails()
# e1.showLanguage() # wrong
e2 = Programmer('Talha', 4)
e2.showDetails()
e2.showLanguage()