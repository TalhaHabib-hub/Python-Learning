'''------------------Python Dictionaries--------------------------'''
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key value pairs that are seperated by commas and enclosed with in curly braces (before python 3.7 dictionaries were unordered)
dic = {
    'apple' : 'saaib',
    "banana" : "kaila",
    324 : "Talha"
}
# dic = {'apple' : 'saaib', "banana" : "kaila", 324 : "Talha"}
print(dic)
print(dic['apple'])
print(dic['banana'])
print(dic[324])

print(dic.get("apple"))#--|-----------------> same work but here is the difference
print(dic['apple'])#______|                                         |
#                                                                   |
#                                                                   |
#       IF for the first one I putted the key which doesn't exist in the dictioary it will just return none but the second one will generate error.


'''now lets say I want to get all the keys it is simple bro'''
print(dic.keys())
'''also simple for the value bro'''
print(dic.values())

# use key values in for loop jani
for i in dic.keys():
    print(i,":",dic[i])
    # print(dic.get(i)) # I think no one should use this way here because the iteration is over the keys (i = keys)


#********ValueError: too many values to unpack (expected 2)****my idea was it
# for i,j in dic.keys() and dic.values():
#     print(i,":",j)
''' for the above three lines hurran i got it'''
'''Oooo bro what if I want the key value pairs together'''
print(dic.items())

for i, j in dic.items():
    print(i," -> ",j)
'''

dic = {
    'apple' : 'saaib',
    "banana" : "kaila",
    324 : "Talha"
}

print(dic['apple'])

print(dic.get("apple"))

print(dic.keys())
        |
print(dic.values())
        |
print(dic.items())

'''