import pandas
print("hi")
print('ta\\ha')
print('talha'[3:5])
print('talha'[3:])
print('zero and empty strings are false')
print('list tuple and dictionaries are false only if they are empty')
string = 0
print(type(string))
print('false')if string  else print('The statment is True')

string = ''
print('false')if string  else print('The statment is True')

list =[]
tuple = ()
dictionary ={}
set = set()

set1 = {1,2,3} ; set2 = {4,5,6}
print(set1.intersection(set2))

print('wrong statment')if list or tuple or dictionary or set else print('the statment is true')
print(list,tuple,dictionary,set)

dict = {'a': 'apple', 'b': 'ball'}
print(dict)
dict.clear()
print(dict)