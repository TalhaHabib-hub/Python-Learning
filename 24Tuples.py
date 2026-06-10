'''--------------------T U P L E  C A N N O T  B E  C H A N G E D------------------'''
tup = (1) # an integer
print(type(tup), tup)

tup = (1,)# a tuple
print(type(tup), tup)

tup = (2, 4, 5, "Talha",False)
print(type(tup), tup)
# tup[0] = 4 # 'tuple' object does not support item assignment

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-2])
print(tup[4])

# checking for elements/ item in a list
if "Talha" in tup:
    print("Yes")
else: 
    print("no")


    '''
      Tuple.append(4)         not going to work
      Tuple.reverse()         not going to work
      Tuple.sort()            not going to work
      Tuple.sort(reverse=True)not going to work
a =   Tuple.index(9)              gonaa to work
print(Tuple.count(3))             going to work
      Tuple.insert(3,503)     not going to work
m =   Tuple.copy()            not going to work
K =   Tuple + m                   going to work--- if both are tuples
m =   Tuple                       going to work----its just assings
Tuple.extend(m)         not going to work
'''
'''-------------------------------------------------------------------------------'''
'''
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets().
Tuples are unchangeabel we can't change them after creation.
'''