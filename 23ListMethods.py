L = [i for i in range(10) if i%2==1]
print('1',L)

L.append(3) # this method for the list will append add the item at the end
print('2',L)

L.reverse() # will reverse our original list
print('3',L)

L.sort()
print('4',L)    # will arrange in asscending order
# for descending do this Talha Jani
L.sort(reverse=True)
print('5',L)

# if Talha I want to find the index of a number in the list what I have to do this:
a = L.index(9)   # 9 at zeroth index
# This method returns the first index of the first occurance of the list
print('6',a)

# now Talha if You want to know how much time an elemnent is comming in the list you will use the count function/ method
print('7',L.count(3))   # as 3 is two times in the list


# here is Talha something not recommended to do but you have to now 
m = L
m[0] = 0
print('8',L) # what I was thinking Talha here is that L list was copied into m then m list form, I changed the first item of m and I was thinking that the L remain unchaged but the result was different because m is becoming the reference of L mean this both are representing one list change in m will cause change in L too.
print('9',m)

# now Talha there comes a question in our mind, what if I want to copy a list and make a seperate list which need to have not such connection with the list from which it is copied
# for that you have to do this gentleman
m = L.copy()
m[3] = 189
print('10',m)
print('11',L)

# Talha if you want to insert an item in the in a particular index use the index method
L.insert(3,503) # pahla nishana lata han phir teer pahnkta han # and will push the other number which is in that index a step ahead
print('12',L)

# this what i did is goning to change the L but if I don't want to change L I can do concatination of two list and make one list in this case the L will not change
K = L + m 
print('13',K)
print('14',L) # L isn't changed
# here is another thing came which is great too
# if you want to add another list into a list use the extend method
L.extend(m) # extend the L with adding m at the end

print('15',L) # L is changed
'''
L.append(4)
L.reverse()
L.sort()
L.sort(reverse=True)
a = L.index(9)
print(L.count(3)) 
m = L
m = L.copy()
L.insert(3,503)
K = L + m 
L.extend(m)
'''