def average(a, b):# a and b here are required arguments
    print('The average is ',(a+b)/2)
average(4, 6)

# there are four type of arguments 
# Default argument
    # def average(a = 4, b = 7):
    #     print('The average is ',(a+b)/2)
    ## average(),average(4,6),average(3),
# keyword arguments
# if you want the order doesn't matter
    # def average(a, b):
    #     print('The average is ',(a+b)/2)
    ## average(b = 7,a =2)
# Required arguments
def add(a, b=6, c=2):
# def add(a, b=6, c): # error
    print(a+b+c)
add(8,7)# so first of all 
# variable arguments
def average(*numbers):# it will take the passed arguments (just have *) a list shown also
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print('Average is :',sum/len(numbers))

average(3 ,5,3,2,4,9,9,3,232,42) # take as much as i want and given accurate result


def namesi(*names):
    namesuu = ''
    for i in names:
        namesuu = namesuu + i # I used concatination here
    print("the name is :",namesuu)

namesi('T','a','l','h','a')

# when will take the argument as a dictionary
# when
def name(**dictla):
    print('hello', dictla["myname"], 'hello2', dictla["hername"] )
    #    _____________________|     _____________________|
name(myname = 'talha', hername = 'ayesha')
# Talha I think it is something new for you because you are sending the whole dictionary to a function but how it works lets present you experience:
    # I called the function 'name' the argument I passed were key value pairs
    # the two starict varible catches the dictionary while the one starisk gets the list 
    # so now as I had to print it for that I use used the parameter as it has gotten the dictionary I wrote the name of the parameter then in square brackets i write the name of the key inside it and this way I got the value
def wordsMeanings(**dictlanawalaarg):# due to sterisk the dictlanawalaarg become a dict inside the function
    print(type(dictlanawalaarg))
    print(f'1.{dictlanawalaarg["apple"]} 2.{dictlanawalaarg['ball']} 3.{dictlanawalaarg['cat']}')

wordsMeanings(apple = "palogh",ball="chandul",cat="pushi")

# the below function is returning

def returnwalafunction(i,k):
    #    i+k #this will cause 'None' output when we call it because there is not the the printing statment and not any returning statment so can say none when useless things happens in our code
    # return 8 # this would skip anything below it self
    return i + k

# returnwalafunction(4,5) #---->
print(returnwalafunction(4,5))
