s = {1, 2, 3, 4}
s2 = (2, 5, 9)
'''union and update''' 
# combining the items of both set A and set B
s3 = s.union(s2) #----------------main--------------thing
print(f's U s2 = {s3}')
print(f' s = {s}, s2 = {s2}')
# here Talha we will say that the s and s2 are untouched 
            # but if we want to update/ add the other set in a set we do this
s.update(s2)     #----------------main--------------thing
print(f' s (updated U) = {s}') 

'''Intersection and intersection_update'''     
#  # the numbers which are in set A and also in B
# also Talha we can do intersection and intersection update
print(f' s = {s} , s3 = {s3} intersection {s.intersection(s3)}')#'''<----'''

print(f' s = {s}, s2 = {s2}')
s.intersection_update(s2)
print(f' s (updated I)  = {s}')
 # the numbers which are in set A and B which are not common
'''symmetric_difference and symmetric_difference update'''
# The symmetric_difference() and symmetric_difference_update()
# methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set
print(f's {s} s3 {s3} ')
s5 = s.symmetric_difference(s3) # it means all the number which are uncommon in both
print("There symmetric difference is",s5)
#  while if I actually want to update symmetric difference in the set so i have to use the update
print(f's {s} s3 {s3} ')
s.symmetric_difference_update(s3)
print(f's (updated S-) {s}')

'''difference() and difference_update()'''
# The difference() and difference_update() methods prints only the items that are only present in the original set and not in both sets.The difference() method returns a new set whereas difference_update() method updates into the existing set from another set. 

A = {3, 5, 3, 32, 3}
B = {5, 2, 3, 23, 39}
print(f'A = {A} B = {B}')
C = A.difference(B)
print('A - B',C)
print('B - A',B.difference(A))
print(f'A = {A} B = {B}')
A.difference_update(B)
print('A =',A) # the numbers which are in set A but not in B 

'''isdisjoint()'''  # these sets have no element in common
# This isdisjoint() method checks if items fo given set are present in another set. This method returns 'False' if items are 'present', else if returns True
B.add(32)
A.add(99)
print(f'A = {A} B = {B}') # if the below statment returns True Talha then the intersection of these set will be an empty set. set()
print('A disjoint B=',A.isdisjoint(B)) # false because the set are joint set A and B have item in common no matter if this joint is because of just one item# '''<----'''

'''issuperset()'''
#  The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns false.
F = A.issuperset(B)
print('F=',F)
'''issubset()'''
 # The issubset() method checks if all the items of The original set are present in the particular set. It returns True if all the items are present, else it returns false.
B.add(99)
F = A.issubset(B)
print('F=',F)
print('A=',A)
'''add() remove() and discord()'''
A.add(839834)

A.remove(839834) # if the number is not present the interpreter will generate error

print('A=',A)
A.discard(32) # if 32 is not present the program will still run without showing error and stopping the whole program

print('A=',A)
#  The difference between reomve and discard is = if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error

'''pop()'''
#  This method removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable
print('B=',B)
k = B.pop() 
print('B=',B)
print('K=',k)
'''' del A '''
del A # use to delete the entire set completely
# print(A) # NameError: name 'A' is not defined
'''clear()'''
# but what if we want to  delete the items not the set (mean if want to make an empty set of a set)
print('B=',B)
B.clear()
print('B=',B)


'''
s3 = s.union(s2)
s.update(s2) 

s4 = s.intersection(s3)
s.intersection_update(s2)

s5 = s.symmetric_difference(s3)
s.symmetric_difference_update(s3)

C = A.difference(B)
A.difference_update(B)

E = A.isdisjoint(B)

F = A.superset(B)

F = A.issubset(B)

B.add(99)
B.remove(99)

A.discard(32)

k = B.pop()

del A

B.clear()
'''
s = {1, 2, 3, 4}
s2 = (2, 5, 9)
s3 = s.union(s2) 
print(f's U s2 = {s3}')
print(f' s = {s}, s2 = {s2}')
s.update(s2)     
print(f' s (updated U) = {s}') 
print(f' s = {s} , s3 = {s3} intersection {s.intersection(s3)}')
print(f' s = {s}, s2 = {s2}')
s.intersection_update(s2)
print(f' s (updated I)  = {s}')
print(f's {s} s3 {s3} ')
s5 = s.symmetric_difference(s3)
print("There symmetric difference is",s5)
print(f's {s} s3 {s3} ')
s.symmetric_difference_update(s3)
print(f's (updated S-) {s}')
A = {3, 5, 3, 32, 3}
B = {5, 2, 3, 23, 39}
print(f'A = {A} B = {B}')
C = A.difference(B)
print('A - B',C)
print('B - A',B.difference(A))
print(f'A = {A} B = {B}')
A.difference_update(B)
print('A =',A) 
B.add(32)
A.add(99)
print(f'A = {A} B = {B}') 
print('A disjoint B=',A.isdisjoint(B)) 
F = A.issuperset(B)
print('F=',F)
B.add(99)
F = A.issubset(B)
print('F=',F)
print('A=',A)
A.add(839834)
A.remove(839834) 
print('A=',A)
A.discard(32) 
print('A=',A)
print('B=',B)
k = B.pop() 
print('B=',B)
print('K=',k)
del A
print('B=',B)
B.clear()
print('B=',B)
