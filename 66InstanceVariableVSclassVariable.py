'''Instances vs class variables
In python, variable can be defined at the class level or at the instance level, Understanding the difference between these types of variable is crucial for writing maintainable and efficient code.

___Class variable___
class variable are defined at the class level an dare shared among all instances of the class. for example a class variable can be used to store the number of instances of a class that have been created.'''

class Employee:
    companyName = "TH" # This one associated with the class
    noOfEmployees = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees+= 1
    def showDetails(self):
        print(f'The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} company is {self.raise_amount}')

emp1 = Employee("Talha")
emp1.raise_amount = 5.4
emp1.showDetails() # here something interesting for you Talha it is exactly the same as below one ""TypeError: Employee.showDetails() takes 0 positional arguments but 1 was given""
'''Talha the reason I mentioned this error for this code here is to show that the code in the line 14 will always be converted to the code at line 16 as here it is clear that we are sending argrments that shows the conversion'''# The error we found we removed the self from the function which we were calling the (showDetails)
# Employee.showDetails(emp1)
emp2 = Employee("Shibli")
emp2.companyName = "MTH"
emp2.showDetails()
'''These all have done to show that  the instances can be for the instances and also can be generic for all the instances so it is better to have one class varible which will have the same value for all the classes'''
# what sir said here is that first of all for a variable is looked as for the instance if the interpreter not finds it then class varible value will be assigned
'''Talha here i spoted the difference'''
# print(Employee.raise_amount)
print(Employee.companyName)

Employee.raise_amount = 0.45
print(Employee.raise_amount)

Employee.companyName = 'Talha.org'
print(Employee.companyName)