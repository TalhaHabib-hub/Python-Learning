'''
Sets are ' unordered collection'(mean there is no guarantee of the ordere you have setted the set in different way but in presenting it can show of in different manner) of data items. They stroe multiple items in a single variable. Set items are seperated by commas and enclosed within curly brackets{and}. ---------S E T S   A R E   U N C H A N G E A B L E----, meaning you cannot change items of the set once created. Sets donnot contain duplicate items
'''
s = {2,4,2,1,"Mehboob Ilahi",True}
print(s) # {2,4,1}---> it will skip the another 2.
# {1, 2, 'Mehboob Ilahi', 4}---> here we can see that the items of set occur in random order and hence they C A N N O T   B E   A C C E S S E D   U S I N G   I N D E X   N U M B E R S . Also sets do sets don't allow duplicate value.
'''-----------------------------maintain order-------------------------------------'''

a = {}# this will get dict
print(type(a))

a = set()
'''empty set'''
print(type(a))
a.add(4)

# a.add(4,5) ----> wrong because takes exactly one argument (2 given)
# a.add(4).add(5).add(6) ----->  'NoneType' object has no attribute 'add'
a.add(7)
a.add(1)
a.add('Sabir')
a.add(2)
print(a)
for i in a:
    print(i)