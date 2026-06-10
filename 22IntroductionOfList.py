'''
Python Lists
. Lists are ordered collection of data items.
. They store multiple items in a single variable.
. List items are seperated by commas and enclosed with in square brackets [  ].
. Lists are C H A N G E A B L E meaning we can alter them after creation.

--------------------T U P L E  C A N N O T  B E  C H A N G E D---------------------
'''
L = [3,5,3,'Talha',True,7,8,9]
print(L)
print(type(L))

print(L[0])
print(L[1]) # like the index of string
print(L[2]) # square bracket notation
print(L[3])
print(L[4])
# name = 'Talha'   # we did this with strings
# print(name[3])

# we can also accessing things with negative indexing as we had done this before with strings
# let i want to access the last one
print(L[-1]) # this will give us a true value

# here is a trick to convert negative index to positive index, just subtract the given negative index from the len of /length of the list the answer will be the positive index pointing the same item as the negative was doing
print(L[-2])          # will print 'Talha'
print(L[len(L)+(-2)]) # will print 'Talha'
print(L[len(L)-2])    # will print 'Talha'
# simply as the length is 5 of the L list
print(L[5-2])         # will print 'Talha'

num = 0

# for i in (len(L)):  # type of Error ---> 'int' object is not iterable
for i in L: # i will be the each item of the list one by one from start
    num += 1
    if (i == 'Talha'):
        print('Yes it is, at index:',num-1)
        break

# it was my try the above one
# but Talha today I learned a very special thing 
# just name the list ask if it is present the interpreter will look on its own and will check the whole list it doesn't required going to each item with using iterations. here it is 
if 'Talha' in L:
    print("Yes it is!")
else:
    print("No it isn't")


# it can also be used in string cases
name = "Talha"
if 'T' in name: 
# if 't' in name:  # t is not in Talha the 'T' is.
    print("a is in",name)
else:
    print("sorry")
# so same things can be done with strings

# here we will discuss Talha how to print
print(L)                            #  [3, 5, 3, 'Talha', True, 7, 8, 9]
print(L[:])                         #  [3, 5, 3, 'Talha', True, 7, 8, 9]
print(L[1:]) #  index 1 to last     #     [5, 3, 'Talha', True, 7, 8, 9]
print((L[1:-1]) == (L[1:len(L)-1])) # True
print(L[1:-1])                      #     [5, 3, 'Talha', True, 7, 8]
print(L[1:len(L)-1])                #     [5, 3, 'Talha', True, 7, 8]
# Talha there also is the Jump index cocept
print(L[1:len(L):2])                #     [5,'Talha', 7 ,9]  
# after printsing a value it will jump twice from this one's index like first printed the %
# Talha I know you Know this one
print((L[-1:-5]) == (L[5:1]))       # True

# hey Talha here is the new dose for you It is delicious
lis = [ i*2 for i in range(5)]      # In the list add i*2 for every i in (0-4)
print(lis)
lis = [ i for i in range(12) if i%2==1 ] # In the list add i for every i in (0-12) while filter out the numbers only whose remenders are 1
print(lis)
lis = [ i*i for i in range(12) if i%2==1 ]
print(lis)