students1 = {"Taha": 503,  "Talh": 513}
students2 = {"Saha": 505,  "kalh": 513}
students1.update(students2) # ubdating a dictionary from another dictionary
print("S1 = ",students1)

students2.clear()
print("S2 = ",students2)

students1.pop('Saha') # This key and its value will be removed, with it you must have to give argument
print("S1 = ",students1)

# also Talha the popitem() will will remove the last key value pair from they end of the dictionary 
students1.popitem()
print("S1 = ",students1)

students2.update({1:4})
print(students2)

del students2[1]
print(students2)

del students2
# print(students2) # NameError: name 'students2' is not defined.
'''
students1.update(students2)

students2.update({1:4})

students2.clear()

students1.pop('Saha')

students1.popitem()

del students2[1]

del students2
'''