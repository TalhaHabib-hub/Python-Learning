a = 4
b = 4
'''_________both are comparison operators_________'''
print(a is b) # exact location of object in memory
# this one is True because python will place three at the same memory location and name them both a and b as they are constant unlike list (the number is mutable)
print(a == b) # value
print('')
i = [1,3,454] # mutable
j = [1,3,454]
print(i is j) # False
print(i == j) # True
print('')
i = (1,3,454) # immutable
j = (1,3,454)
print(i is j) # True
print(i == j) # True
print('')
i = 'Talha' # immutable
j = 'Talha'
print(i is j) # True
print(i == j) # True
print('')
i = None # immutable
j = None
print(i is j) # True
print(i == j) # True

'''simple Talha bro! all the objects which are the same and are immutable their doing is will return True and for the one which are mutable doing there is will return false'''
# here is by sir jani 
# In python, is and == both are comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.
# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the object being compared are exact same object in memory, while == will return True if the objects have the same value.