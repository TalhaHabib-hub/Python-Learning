'''-------------------------Tuple is immutable-------------------------------'''
# I am trying to change a tuple , and I did but indirectly
tup = (3,5,3,2)
print(tup)

put = list(tup)
put[2] = 56
tup = tuple(put)

print(tup)

tur = tup + (4323,)
print(tur)
'''----------------------------methods-------------------------------------'''
tuple = (3,3,3,2,2,2,2,3,3,3,1,2)
print(tuple.count(3))
# now if I am wanting to get that at what position is of 3 from 4 to the 8th index 
print(tuple.index(3, 4,   9)) # search the index of 3 from 4 to 9-1 and tell the index of 3        |   |___'''''''|
'''   tuple.index(element,start,end)'''
print(tuple.index(1),'th')


print(len(tuple))