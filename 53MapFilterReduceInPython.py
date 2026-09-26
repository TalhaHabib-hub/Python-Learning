'''In python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

map
The map function applies a function to each element (the function will be written first as argument to the map function) in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax

map(function, iterable)'''
# here is a function Talha for you
def cube (x):
    return x*x*x
print(cube(2))
# the above one is simple Talha but what if you have a list like 
l = [4,3,2,2,4,2,5,2]
# now you are wanting what should I do so that in place of all these items I would get their cubes 
# we can do with for loop
'''
j = []
for i in l:
    j.append(cube(i))
print(j)
'''
# no jani it seems very long to me but I also have a short cut why not we should try that one
j = map(cube, l) # <map object at 0x00000226160D9740> # returning a map object # this is working like this I am sending cube function to map function (built-in) , also a list the map function will go at each item of the list make the cube of them (will apply the function on the elements of the list and return a map object which if we type cast to list will get us our list)
print(j)
j = list(map(cube, l) ) # [64, 27, 8, 8, 64, 8, 125, 8]
print(j)
j = list(map(lambda x:x**3,l) ) # [64, 27, 8, 8, 64, 8, 125, 8]
print(j)

'''Filter
The filter function filters a sequence of element based on a given ''''''predicate'''''' (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

'''
# ffunction = lambda x: x>4 the filter function is not concedering ffunction as a function so let me do it this way or
# filter( lambda x: x>4,l)
#  # so we have to do the above instead of the nam of  the lamda function's name we can name here only the function which are not defined the way lambda functions are defined
def ffunction (x):
    return x>4
print(filter(ffunction,l)) #<filter object at 0x0000019B661816F0>
print(list(filter(ffunction,l)))
''' Look Talha jigar I am explaining this way 
first the built-in filter function, lets say I am thorwing the function which returns true or false and secondly throwing a list , what the filter function is gonna do is will return only the list of the number for which the function has returned true'''
'''reduce 
The reduce function is a higher-order function that applies a function to a sequence and returns a single value it is the part of the functool module in python and has the following sequence'''

from functools import reduce

print(reduce(lambda x,y: x+y,l)) # jani hum reduce han apka map or filter ki tarah nahi ka bhai saab reduce object return karan hamaran ahsaanaat yad rakho , ok bhi koi nahi sara aisa han
'''
[4,3,2,2,4,2,5,2]
[7,2,2,4,2,5,2]
[9,2,4,2,5,2]
[11,4,2,5,2]
[15,2,5,2]
[17,5,2]
[22,2]
[24]

'''
