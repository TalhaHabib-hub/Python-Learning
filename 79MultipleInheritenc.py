# when we inherit a class from more than one class is called multiple inheritence
class Employee:
    def __init__(self, name):
        self.name  = name
    def show(self):
        print(f'The name is {self.name}')
class Dancer:
    def __init__(self, dance):
        self.dance  = dance
    def show(self):
        print(f'The dance is {self.dance}')

class DancerEmployee(Employee,Dancer): # in this case the show of the Employee will be executed 
# class DancerEmployee(Dancer,Employee): # in this case the show of the dancer will be executed # and also Talha look that mro is changing for them as well
     def __init__(self, name,dance):
        self.name  = name
        self.dance  = dance

o = DancerEmployee('kathak','shiwami')
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())
# mro = mathod resoultion order

# for line number 14 [<class '__main__.DancerEmployee'>, <class '__main__.Dancer'>, <class '__main__.Employee'>, <class 'object'>]

# for line number 13 [<class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]