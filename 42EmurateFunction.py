
cars = ['lambo','mercedes','pagani','fortuner']
i = 0
for car in cars:
    print(car)
    if(i==3):
        print("Talha's first car.")
    i += 1
print('')
# Talha the using enumerate function is the simple of using the same logic without the extra variable made out side the loop
for i,car in enumerate(cars):
    print(i,car)
    if(i==3):
        print(i,"Talha's first car.")
print('')

'''Enumerate function in python''' # Enumerate == specify individually
# The enumerate function is a built-in function in python that allows you to loop over a sequence(such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.

car = ['lambo','mercedes','pagani','fortuner']
# for i, car in car:  -------> this is not working properly
for i, car in enumerate(car):
    print(i,car)

    '''As you see Talha, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above'''

print("")
name = 'Talha Habib'
for i, A in enumerate(name):
    print(i,'-->',A)


# for the enumerate function starts at the index 0, but you can specify a different starting index by passing it as an arggument to the enumerate function.
print("")
name = 'Shaheen-e-Islam'
for i, A in enumerate(name, start=2): # index 2 sa start hoga na ka the A
    print(i,'-->',A)

tuple = (1,4,2,2,1,4,3,3,2,2)
for i,v in enumerate(tuple,start=1):
    print(i,"->",v)

# but Talha remeber not to forget the positons