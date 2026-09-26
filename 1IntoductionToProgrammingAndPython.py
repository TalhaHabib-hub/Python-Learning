# no code just introduction
# comparison operators
print(0 or 1)
print(False or 'hey')
print('hi' or 'hey') # takes the first one
print([] or False)
print(False or [])

print('__________')
print(0 and 1)
print(False and 'hey')
print('hi' and 'hey') # takes the first one
print([] and False)
print(False and [])

# way of using the ternary operatoar instead of if else statment
# this one is an if else statment I will write its ternary statment late
def is_adult(age):
    if age > 18 :
        return True
    else :
        return False
    
# so I can also write this statment in the form of ternary operator
def is_adult_2 (age):
    return True if age > 18 else False

print(is_adult(34))
print(is_adult_2(34))

name = 'Talha'
name+=' is my name'
print(name)
print(f'''{name}
h  ow is it going
      
      I am Talha''')

print('talha habib'.title())