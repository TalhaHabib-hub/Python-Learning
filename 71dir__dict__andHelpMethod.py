'''doing object intospection'''
# dir(), __dict__, help()

# x = [3,2,1,5]  #list
# print(dir(x))
# print((x.__add__))

# x = (3,2,1,5) #tuple
# print(dir(x))
# print((x.__add__))
# so the dir() function returns a list of all the attributes and methods (including dunder methods) the __istarahKaFunction__ available for an object. It is a useful tool for discovering what you can do with an object
# 
 
'''
import Talha57friend
print(dir(Talha57friend)) 
'''
# at the end of this result i can see the function which i maded in this module
'''lets now go for the dict method/attributes is also called by sir to it'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('Talha',21)
# p.__dict__
print(p.__dict__) # this is actually returning me the variable and the value assigned to them in key value pair form means in the form of dictionary
print(help(Person))
'''help() function is used to get help documentation for an object, including a description of its attributes and methods'''
print(help(str))